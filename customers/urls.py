from django.urls import path, include


from customers.views import CustomerDetailUpdateDelete, CustomerListCreate

urlpatterns = [
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailUpdateDelete.as_view(), name='customer-detail'),
]