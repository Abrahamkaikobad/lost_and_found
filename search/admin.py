from django.contrib import admin

# Register your models here.
from .models import FoundItem,Category,LostItem

admin.site.register(FoundItem)
admin.site.register(Category)
admin.site.register(LostItem)

