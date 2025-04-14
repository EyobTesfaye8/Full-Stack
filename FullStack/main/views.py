from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "main/x-base.html")

def signUp(request):
    return render(request, 'main/signUp.html')

def login(request):
    return render(request, 'main/login.html')

def UserHome(request, string):
    return render(request, "main/x-base.html")
