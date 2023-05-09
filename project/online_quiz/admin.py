from django.contrib import admin
from . models import Student,Teacher,Course,Question,Result
# Register your models here.
admin.site.register([Student,Teacher,Course,Question,Result])
