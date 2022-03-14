from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.


def login(request):

    return render(request, 'login.html')
