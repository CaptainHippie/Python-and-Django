from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50,unique=True,null=False)
    username = models.CharField(max_length=50,unique=True,null=False)
    password = models.CharField(max_length=50,null=False)