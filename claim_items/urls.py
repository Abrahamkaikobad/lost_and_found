from django.urls import path,include
from .views import render_lost_Items,contact

urlpatterns = [
path('claim/',render_lost_Items,name="Claim-Items"),
path('claim_form/',contact,name='claim-form')

]