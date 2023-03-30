from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length = 256)
    # password = models.CharField(max_length=56)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.name}'
    
class free_trucks(models.Model):
    truck_num = models.IntegerField()
    
    def __str__(self):
        return f'{self.truck_num}'
