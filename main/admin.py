from django.contrib import admin

# Register your models here.
from .models import MainText, Module

admin.site.register(MainText)
admin.site.register(Module)