from django.contrib import admin

# Register your models here.
from .models import Order, OrderSMS

admin.site.register(Order)
admin.site.register(OrderSMS)
