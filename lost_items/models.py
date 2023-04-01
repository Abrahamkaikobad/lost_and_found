from django.db import models
from django.contrib.auth.models import User

class LostItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    lost_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    is_found = models.BooleanField(default=False)
