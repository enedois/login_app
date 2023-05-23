from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register_user(request):
    return render(request,'authenticate/register_user.html')


def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

