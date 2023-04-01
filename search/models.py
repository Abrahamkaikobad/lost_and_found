from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now


class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    
   

class FoundItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)
   
    def __str__(self):
     return self.name
    

class Category(models.Model):
   id=models.AutoField(primary_key=True)
   name=models.CharField(max_length=50)
   
   def get_all_category():
      return Category.objects.all()
   

   def __str__(self):
      return self.name

    
class LostItem(models.Model):
   name=models.CharField(max_length=50)
   category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
   description=models.CharField(max_length=200,default="",blank=True,null=True)
   #image=models.ImageField(upload_to='images/',default="")

   def __str__(self):
      return self.name
   
