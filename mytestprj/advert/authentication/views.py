from django.http import Http404
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from .serializers import UserSerializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@extend_schema(tags=["Authentication"])
class RegisterView(APIView):
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response()
        response.data = {'access_token': access_token}
        return response

@extend_schema(tags=["Authentication"])
class LoginView(APIView):
    queryset = User.objects.all()

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise Http404("User not found!")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response()
        response.data = {'access_token': access_token}
        return response

@extend_schema(tags=["Authentication"])
class UserView(APIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializers(request.user)
        return Response(serializer.data)

@extend_schema(tags=["Authentication"])
class LogoutView(APIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            raise AuthenticationFailed('Refresh token is required for logout.')

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            raise AuthenticationFailed('Invalid refresh token.')

        response = Response({'detail': 'Logout successful.'})
        return response


class UserDetail(generics.GenericAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()

    @extend_schema(tags=["Authentication"])
    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except:
            return None

    @extend_schema(tags=["Authentication"])
    def get(self, request, user_id):
        """
        Получение записи CustomUser
        """
        user = self.get_user(user_id)
        if user is None:
            return Response({"status": "fail", "error": f"Пользователь с id: {user_id} не найден"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(user)
        return Response({"status": "success", "data": {"user": serializer.data}})


