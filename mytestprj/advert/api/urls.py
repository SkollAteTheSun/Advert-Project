from django.urls import path
from .views import *

urlpatterns = [
    path('adverts/', Adverts.as_view(), name='adverts-list'),
    path('adverts/import-csv/', Adverts.as_view(), name='import-adverts-csv'),

    path('adverts/<int:advert_id>/', AdvertDetail.as_view(), name='advert-detail'),
    path('adverts/<int:advert_id>/proposals', AdvertProposalsAPIView.as_view(), name='advert-proposals'),

    path('categories/', Categories.as_view(), name='categories-list'),
    path('categories/<int:category_id>/', CategoryDetail.as_view(), name='category-detail'),

    path('proposals/', Proposals.as_view(), name='proposals-list'),
    path('proposals/<int:proposal_id>/', ProposalDetail.as_view(), name='proposal-detail'),
    path('proposals/<int:proposal_id>/accept/', AcceptProposalAPIView.as_view(), name='accept-proposal'),
]
