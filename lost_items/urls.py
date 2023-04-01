from django.urls import path
from . import views

urlpatterns = [
    path('lost-items/<int:id>/', views.lost_item_detail, name='lost_item_detail'),
    path('search/', views.search, name='search'),
    path('search/results/', views.search_results, name='search_results'),
]
