from django.contrib import admin

from .models import Vehicle, VehicleType

# Register your models here.

admin.site.register(VehicleType)
admin.site.register(Vehicle)