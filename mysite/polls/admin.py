from django.contrib import admin

from .models import Question,Choice

admin.site.register([Question,Choice])
# Register your models here.
