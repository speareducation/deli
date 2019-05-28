from django.contrib import admin

# Register your models here.
from .models import Sandwich,Topping

admin.site.register(Sandwich)
admin.site.register(Topping)