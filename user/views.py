from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView

class UserRegisterView(CreateView):
    model      = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'
    success_url   = reverse_lazy('post:list')

class UserLoginView(LoginView):
    template_name   = 'user/login.html'

class UserLogoutView(LogoutView):
    template_name   = 'user/logout.html'