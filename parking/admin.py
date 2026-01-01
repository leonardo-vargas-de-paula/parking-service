from django.contrib import admin
from .models import ParkingSpot, ParkingRecord
# Register your models here.

admin.site.register(ParkingSpot)
admin.site.register(ParkingRecord)