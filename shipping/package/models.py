from django.db import models
from datetime import date, timedelta

# Create your models here.
def five_days_from_now():
    return date.today() + timedelta(days=5)

class Package(models.Model):
    phone = models.IntegerField(max_length=50)
    address = models.CharField(max_length=250)
    status = models.CharField(max_length = 50, default='Received')
    eta = models.DateField(default=five_days_from_now)
#su=owner,sai@1234
# user=postmaster
# password=sri@1234
