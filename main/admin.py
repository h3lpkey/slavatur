from django.contrib import admin

# Register your models here.
from .models import MainText, Module, Comment

admin.site.register(Comment)
admin.site.register(MainText)
admin.site.register(Module)