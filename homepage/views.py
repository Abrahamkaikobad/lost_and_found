from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def navbar(request):
    return render(request,'homepage/navbar.html')




