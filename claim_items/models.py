from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
