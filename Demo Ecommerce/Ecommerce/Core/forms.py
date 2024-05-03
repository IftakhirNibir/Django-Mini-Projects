from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username','first_name','last_name','email', 'password1', 'password2')


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your firstname',
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your lastname',
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'form-control'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control'
    }))