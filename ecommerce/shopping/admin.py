from django.contrib import admin
from . models import product_data,customer,cart
# Register your models here.
admin.site.register([product_data,customer,cart])
