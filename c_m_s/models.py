from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.IntegerField()
    email=models.EmailField(max_length=50)
    city=models.CharField(max_length=50)

def __str__(self):
    return self.name

