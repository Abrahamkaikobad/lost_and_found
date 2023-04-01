from django.urls import path,include
from . import views

urlpatterns=[
    path('Homepage',views.navbar)    
]