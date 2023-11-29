from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .models import *
from .serializers import *



@extend_schema(tags=["Authentication"])
class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomUserSerializer


class UserAuthenticationAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomUserLoginSerializer

    @extend_schema(tags=["Authentication"])
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            serializer = CustomUserLoginSerializer(user)
            return Response({'status': 'success', 'result': serializer.data})
        else:
            return Response({'status': 'fail', 'error': 'Неверные данные', 'result': None})


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    @extend_schema(tags=["Authentication"])
    def post(self, request):
        logout(request)
        return Response({"status": "success", "message": "Пользователь успешно вышел из аккаунта"})


class UserDetail(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


    @extend_schema(tags=["Authentication"])
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(id=user_id)
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
