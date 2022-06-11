from django.db import models

# Create your models here.
class Book(models.Model):
    acc_no = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    def __str__(self):
       return self.acc_no
