from django.urls import path,include
from .views import render_lost_Items,contact,show_profile,delete_item,edit_item

urlpatterns = [
path('claim/',render_lost_Items,name="Claim-Items"),
path('claim_form/',contact,name='claim-form'),
path('claimers/',show_profile,name='profile-show'),
 
 #these 2 path edit later
 #path('claimers/<int:item_id>/delete/', delete_item, name='delete_item'),
 #path('claimers/<int:item_id>/edit/', edit_item, name='edit_item'),

]