from rest_framework import viewsets
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer
from core.permissions import IsOwnerOfVehicleOrRecord
from rest_framework.permissions import DjangoModelPermissions

class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]
    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff:
            return ParkingRecord.objects.all()   
        return ParkingRecord.objects.filter(vehicle__owner__user=user)


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer