from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from customers.models import Customer
from customers.serializers import CustomerSerializer

#findall - get all customers
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    list_permission_classes = [DjangoModelPermissions, IsAdminUser]