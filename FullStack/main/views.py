from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from . import backends
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    users = User.objects.all().order_by('-firstName')
    context = {
    'contents':users
}
    return render(request, "main/base.html", context)

# def login(request):
#     return render(request, 'main/login_page.html')

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
        users = User.objects.all().order_by('firstName')
        context = {
        'users':users
    }
        return render(request, "main/base.html", context)
    
class Login(View):
    def get(self, request):
        return render(request, 'main/login_page.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            return redirect('UserHome', pk = user.get_user_id())
        else:
            messages.error(request, ("fuck NO"))
            return redirect('login')
        # user authentication here!!!