from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def HomePage(request):
    return render(request, 'registration/index.html', {})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fullname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(uname, email, password)
       
        new_user.save()
        return redirect('login-page')
  
    return render(request, 'registration/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
             messages.error(request, 'Invalid username or password.')
        return redirect('login-page')

    return render(request, 'registration/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'registration/test.html', {})

#extra here