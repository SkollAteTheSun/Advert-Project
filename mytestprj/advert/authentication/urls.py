from django.urls import path
from .views import *

urlpatterns = [
    path('authentication/', UserRegistrationAPIView.as_view(), name='authentication'),
    path('login/', UserAuthenticationAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:user_id>', UserDetail.as_view(), name='user-detail'),
]