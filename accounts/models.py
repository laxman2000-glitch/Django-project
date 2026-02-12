from django.db import models
from django.contrib.auth.models import User

    
    
class Details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user.username}-{self.name}"
