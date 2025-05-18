from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {"firstName","lastName","email","password"}
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {"email", "password"}
