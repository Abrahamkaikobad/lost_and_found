from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('homepage.urls')),
    path('', include('auth_system.urls')),
    #path('',include('practice.urls')),
    #path('', include('lost_items.urls')),
    path('', include('search.urls')),
    path('', include('week4_notification.urls')),
    path('',include('claim_items.urls')),
    
]
    
    

