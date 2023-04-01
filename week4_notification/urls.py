from django.urls import path,include
from .views import test,success


urlpatterns = [
    path('notification/', test,name='notification')
]
    