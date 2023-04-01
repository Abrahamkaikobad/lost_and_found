from django.urls import path,include
from .views import *
#for image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('search/',SearchView.as_view(),name='search-page'),
    path('filter/<int:category_id>/',filter,name="filter")  ,
    
     
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
