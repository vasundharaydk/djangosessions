from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    phone_number = models.IntegerField()
    delivery_address = models.CharField(max_length=250)
    package_id = models.CharField(max_length=20 ,unique=True)
    status = models.CharField(max_length=40)

class Postman(models.Model):
    user_name = models.CharField(max_length=50 ,unique=True)
    password = models.CharField(max_length=20)
    