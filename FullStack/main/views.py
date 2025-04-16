from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, "main/base.html")

def signUp(request):
    return render(request, 'main/signup_page.html')

def login(request):
    return render(request, 'main/login_page.html')

def UserHome(request, string):
    return render(request, "main/base.html")
