from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='authentication'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
    path('<int:user_id>', UserDetail.as_view(), name='user-detail'),
]