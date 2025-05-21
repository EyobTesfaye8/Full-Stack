from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.views import View
# Create your views here.

Sform = SignUpForm()
Lform = LoginForm()
users = User.objects.all().order_by('firstName')

def home(request):
    Sform = SignUpForm()
    Lform = LoginForm()
    users = User.objects.all().order_by('-firstName')
    context = {
    "Sform": Sform,
    'Lform': Lform,
    'contents':users
}
    return render(request, "main/base.html", context)

def login(request):
    return render(request, 'main/login_page.html')

def UserHome(request, pk):
    user = User.objects.get(id = pk)
    context = {'user':user}
    return render(request, "main/usersHome.html", context)

class SignUp(View):
    def get(self, request):
        return render(request, 'main/signup_page.html') 
    def post(self, request):
        # template_name = 'signup_page.html'
        Sform = SignUpForm()
        context = {
        "Sform": Sform,
    }
        form = SignUpForm(request.POST);
        if form.is_valid():
            form.save()
            messages.success(request, ("signed up successfully"))
            return redirect ('home')
        else:
            messages.error(request, ("please, fill out the form correctly!!!"))
            return render(request, 'main/signup_page.html', context)
    
class Home(View):
    def get(self, request):
        users = User.objects.all().order_by('-firstName')
        context = {
        'users':users
    }
        return render(request, "main/base.html", context)
    
class Login(View):
    def get(self, request):
        return render(request, 'main/login_page.html')
    def post(self, request):
        form = LoginForm(request.POST)
        users = User.objects.all('email', 'password')
        context = {
            'users':users
        }
        
        # user authentication here!!!