from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.signUp, name='sign up'),
    path('log-in/', views.login, name='login'),
    path('username/<str:Uname>/', views.UserHome, name='UserHome'),
]