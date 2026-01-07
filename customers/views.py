from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from customers.models import Customer
from customers.serializers import CustomerSerializer
from customers.filters import CustomerFilterClass
from rest_framework import generics


#findall - get all customers
'''
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    rql_filter_class = CustomerFilterClass
    list_permission_classes = [DjangoModelPermissions, IsAdminUser]
'''
class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    rql_filter_class = CustomerFilterClass
    action = 'list'

class CustomerDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    rql_filter_class = CustomerFilterClass
    action = 'retrieve'