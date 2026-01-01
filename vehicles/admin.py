from django.contrib import admin

from .models import Vehicle, VehicleType

# Register your models here.

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'model']
    search_fields = ['model', 'license_plate']
    list_filter=['vehicle_type']