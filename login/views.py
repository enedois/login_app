from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def register_user(request):
    return render(request,'authenticate/register_user.html')


def home(request):
    return render(request, 'home.html', {})