from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.views import APIView

from .models import *
from .serializers import *


class Categories(generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


    @extend_schema(tags=["Category"])
    def get(self, request):

        name_param = request.GET.get('name')

        categories = Category.objects.all()

        if name_param:
            categories = categories.filter(name__icontains=name_param)
        serializer = self.serializer_class(categories, many=True)

        return Response({
            "status": "success",
            "categories": serializer.data
        })


    @extend_schema(tags=["Category"])
    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if not request.user.is_superuser:
            return Response({"status": "fail", "message": f"У вас нет доступа к созданию категорий"},
                            status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"category": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(tags=["Category"])
    def get_category(self, category_id):
        try:
            category = Category.objects.get(id=category_id)
            return category
        except:
            return None

    @extend_schema(tags=["Category"])
    def get(self, request, category_id):

        category = self.get_category(category_id)
        if category is None:
            return Response({"status": "fail", "message": f"Категория с id: {category_id} не найдена"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(category)
        return Response({"status": "success", "data": {"category": serializer.data}})


    @extend_schema(tags=["Category"])
    def patch(self, request, category_id):

        category = self.get_category(category_id)
        if category is None:
            return Response({"status": "fail", "message": f"Категория с id: {category_id} не найдена"},
                            status=status.HTTP_404_NOT_FOUND)

        if not request.user.is_superuser:
            return Response({"status": "fail", "message": f"У вас нет доступа к категории с id: {category_id}"},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"category": serializer.data}})

        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    @extend_schema(tags=["Category"])
    def delete(self, request, category_id):

        category = self.get_category(category_id)
        if category is None:
            return Response({"status": "fail", "message": f"Категория с id: {category_id} не найдена"},
                            status=status.HTTP_404_NOT_FOUND)

        if not request.user.is_superuser:
            return Response({"status": "fail", "message": f"У вас нет доступа к категории с id: {category_id}"},
                            status=status.HTTP_403_FORBIDDEN)

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Adverts(generics.GenericAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()

    @extend_schema(tags=["Advert"])
    def get(self, request):

        name_param = request.GET.get('name')

        category_param = request.GET.get('category')

        adverts = Advert.objects.all()

        if name_param:
            adverts = adverts.filter(name__icontains=name_param)

        if category_param:
            adverts = adverts.filter(category=category_param)

        serializer = self.serializer_class(adverts, many=True)

        return Response({
            "status": "success",
            "adverts": serializer.data
        })

    @extend_schema(tags=["Advert"])
    def post(self, request):

        if not request.user.is_authenticated:
            return Response({"status": "fail", "message": "Войдите в аккаунт"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"advert": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AdvertDetail(generics.GenericAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


    @extend_schema(tags=["Advert"])
    def get_advert(self, advert_id):
        try:
            return Advert.objects.get(id=advert_id)
        except:
            return None


    @extend_schema(tags=["Advert"])
    def get(self, request, advert_id):

        advert = self.get_advert(advert_id)
        if advert is None:
            return Response({"status": "fail", "message": f"Объявление с id: {advert_id} не найдено"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(advert)
        return Response({"status": "success", "data": {"advert": serializer.data}})


    @extend_schema(tags=["Advert"])
    def patch(self, request, advert_id):

        advert = self.get_advert(advert_id)
        if advert is None:
            return Response({"status": "fail", "message": f"Объявление с id: {advert_id} не найдено"},
                            status=status.HTTP_404_NOT_FOUND)

        if advert.user != request.user:
            return Response({"status": "fail", "message": f"У вас нет доступа к объявлению с id: {advert_id}"},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(advert, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"advert": serializer.data}})

        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    @extend_schema(tags=["Advert"])
    def delete(self, request, advert_id):

        advert = self.get_advert(advert_id)
        if advert is None:
            return Response({"status": "fail", "message": f"Объявление с id: {advert_id} не найдено"},
                            status=status.HTTP_404_NOT_FOUND)

        if (advert.user != request.user) or (not request.user.is_superuser):
            return Response({"status": "fail", "message": f"У вас нет доступа к объявлению с id: {advert_id}"},
                            status=status.HTTP_403_FORBIDDEN)

        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Proposals(generics.GenericAPIView):
    serializer_class = ProposalSerializer
    queryset = Proposal.objects.all()


    @extend_schema(tags=["Proposal"])
    def get(self, request):

        proposals = Proposal.objects.all()

        serializer = self.serializer_class(proposals, many=True)

        return Response({
            "status": "success",
            "proposals": serializer.data
        })


    @extend_schema(tags=["Proposal"])
    def post(self, request):

        if not request.user.is_authenticated:
            return Response({"status": "fail", "message": "Войдите в аккаунт"}, status=status.HTTP_400_BAD_REQUEST)

        advert_id = request.data['advert']
        advert_author = Advert.objects.get(id=advert_id).user

        if request.user == advert_author:
            return Response({"status": "fail", "message": "Нельзя создать заявку на свое объявление"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"proposal": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProposalDetail(generics.GenericAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


    @extend_schema(tags=["Proposal"])
    def get_proposal(self, proposal_id):
        try:
            return Proposal.objects.get(id=proposal_id)
        except:
            return None


    @extend_schema(tags=["Proposal"])
    def get(self, request, proposal_id):

        proposal = self.get_proposal(proposal_id)
        if proposal is None:
            return Response({"status": "fail", "message": f"Заявка с id: {proposal_id} не найдена"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(proposal)
        return Response({"status": "success", "data": {"proposal": serializer.data}})


    @extend_schema(tags=["Proposal"])
    def patch(self, request, proposal_id):

        proposal = self.get_proposal(proposal_id)
        if proposal is None:
            return Response({"status": "fail", "message": f"Заявка с id: {proposal_id} не найдена"},
                            status=status.HTTP_404_NOT_FOUND)

        if proposal.user != request.user:
            return Response({"status": "fail", "message": f"У вас нет доступа к заявке с id: {proposal_id}"},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.serializer_class(proposal, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"proposal": serializer.data}})

        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    @extend_schema(tags=["Proposal"])
    def delete(self, request, proposal_id):

        proposal = self.get_proposal(proposal_id)
        if proposal is None:
            return Response({"status": "fail", "message": f"Заявка с id: {proposal_id} не найдена"},
                            status=status.HTTP_404_NOT_FOUND)

        if (proposal.user != request.user) or (not request.user.is_superuser):
            return Response({"status": "fail", "message": f"У вас нет доступа к заявке с id: {proposal_id}"},
                            status=status.HTTP_403_FORBIDDEN)

        proposal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AcceptProposalAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)


    @extend_schema(tags=["Proposal"])
    def post(self, request, proposal_id):

        proposal = Proposal.objects.get(id=proposal_id)

        if proposal is None:
            return Response({"status": "fail", "message": f"Заявка с id: {proposal_id} не найдена"},
                            status=status.HTTP_404_NOT_FOUND)

        advert = Advert.objects.get(id=proposal.advert.id)

        if advert is None:
            return Response({"status": "fail", "message": f"Объявление для этой заявки не найдено"},
                            status=status.HTTP_404_NOT_FOUND)

        if len(Proposal.objects.filter(advert=advert.id, accepted=True)) == 0:
            proposal.accepted = True
            proposal.save()

            return Response({'status': 'success', 'message': 'Вы приняли заявку'})

        else:
            return Response({"status": "fail", "message": f"Для этого объявления уже принята заявка"},
                            status=status.HTTP_403_FORBIDDEN)

class AdvertProposalsAPIView(APIView):
    serializer_class = ProposalSerializer

    @extend_schema(tags=["Advert"])
    def get(self, request, advert_id):

        proposals = Proposal.objects.filter(advert=advert_id)

        serializer = self.serializer_class(proposals, many=True)

        return Response({
            "status": "success",
            "proposals": serializer.data
        })
