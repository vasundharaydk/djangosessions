from django.contrib import admin
from . models import Course,Question,Result
from django.contrib.auth.models import Permission
# Register your models here.
admin.site.register([Course,Question,Result])
admin.site.register(Permission)

