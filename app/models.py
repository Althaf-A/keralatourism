from django.db import models

# Create your models here.
class akm(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=30)
    password=models.EmailField(max_length=30)
    confirmpassword=models.EmailField(max_length=30,default='')