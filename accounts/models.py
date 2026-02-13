from django.db import models
from django.contrib.auth.models import User

    
    
class Details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user.username}-{self.name}"

class Shiva(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    fathername= models.CharField(max_length=255)
    email= models.EmailField()
    mobilenumber=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}-{self.firstname}+{self.lastname}-{self.fathername}-{self.email}-{self.mobilenumber}"


