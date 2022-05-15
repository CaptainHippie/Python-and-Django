from django.db import models

# Create your models here.

class userreg(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30,unique=True)
    uname=models.CharField(max_length=30,unique=True)
    passwd=models.CharField(max_length=30)
    class Meta:
        db_table = "data_table"