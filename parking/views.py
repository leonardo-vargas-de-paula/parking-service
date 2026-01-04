from rest_framework import viewsets
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer
from core.permissions import IsOwnerOfVehicleOrRecord
from rest_framework.permissions import DjangoModelPermissions
from parking.filters import ParkingRecordFilterClass, ParkingSpotFilterClass
from rest_framework import generics


class ParkingSpotListCreate(generics.ListCreateAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    rql_filter_class = ParkingSpotFilterClass
    action = 'list'


class ParkingSpotDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    rql_filter_class = ParkingSpotFilterClass
    action = 'retrieve'
    

class ParkingRecordListCreate(generics.ListCreateAPIView):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    rql_filter_class = ParkingRecordFilterClass
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]
    action = 'list'
    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff:
            return ParkingRecord.objects.all()   
        return ParkingRecord.objects.filter(vehicle__owner__user=user)

class ParkingRecordDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    rql_filter_class = ParkingRecordFilterClass
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]
    action = 'retrieve'
    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff:
            return ParkingRecord.objects.all()   
        return ParkingRecord.objects.filter(vehicle__owner__user=user)

    
    