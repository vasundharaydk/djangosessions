from django.contrib import admin
from . models import Customer,Postman

# Register your models here.
admin.site.register([Customer,Postman])
