from django.db import models

# Create your models here.
class Package(models.Model):
    phone = models.IntegerField(max_length=50)
    address = models.CharField(max_length=250)