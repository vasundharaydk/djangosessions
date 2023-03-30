from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length = 256)
    #
    # password = models.CharField(default='password', max_length=56)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def _str_(self):
        return f'{self.name}'

class Attendance(models.Model):
    date_field = models.DateField()
    attendance = models.CharField(max_length=256)
    employees = models.ForeignKey(Employees,on_delete=models.CASCADE)

    def _str_(self):
        return f'{self.employees} - {self.data_field} - {self.attendance}'