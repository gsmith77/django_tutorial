from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    
class Persons(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)