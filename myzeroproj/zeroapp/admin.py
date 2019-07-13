from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import signup

# Register your models here.
from . models import city
class cityname(admin.ModelAdmin):
    list_display = ['id','cyty','counrycode','district','population',]
    class META:
        model=city
admin.site.register (city)

from . models import signup
admin.site.register (signup)