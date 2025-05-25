from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/',SignUp.as_view(), name='sign up'),
    path('login/', Login.as_view(), name='login'),
    path('user/<int:pk>/', UserHome, name='UserHome'),
]