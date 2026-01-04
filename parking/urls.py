from django.urls import path, include
from parking.views import ParkingRecordDetailUpdateDelete, ParkingRecordListCreate, ParkingSpotDetailUpdateDelete, ParkingSpotListCreate


urlpatterns = [
    path('parking/spots/', ParkingSpotListCreate.as_view(), name='parking-spot-list-create'),
    path('parking/spots/<str:spot_number>/', ParkingSpotDetailUpdateDelete.as_view(), name='parking-spot-detail'),
    path('parking/records/', ParkingRecordListCreate.as_view(), name='parking-record-list-create'),
    path('parking/records/<int:pk>/', ParkingRecordDetailUpdateDelete.as_view(), name='parking-record-detail'),
]