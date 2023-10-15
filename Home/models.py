from django.db import models
from django.contrib.auth.models import User
from msilib.schema import Class

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    message = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name
    
