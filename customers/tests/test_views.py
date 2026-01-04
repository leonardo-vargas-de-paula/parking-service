from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import Customer

class CustomerAPITest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin_test',
            password='password123',
            email='admin@parking.com'
        )
        
        refresh = RefreshToken.for_user(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
        self.customer_data = {
            "name": "João da Silva",
            "cpf": "123.456.789-00",
            "phone": "(67) 99999-9999"
        }
        
        self.customer = Customer.objects.create(name="Maria Souza", cpf="000.111.222-33")
        self.list_url = reverse('customer-list-create')
        self.detail_url = reverse('customer-detail', kwargs={'pk': self.customer.id})
        
    def test_unauthenticated_access(self):
        self.client.credentials()  
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_customer_success(self):
        response = self.client.post(self.list_url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.customer_data['name'])

    def test_create_customer_missing_required_field(self):
        data = {"cpf": "123"} 
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    def test_list_customers(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)


    def test_partial_update_customer(self):
        payload = {"phone": "99999-0000"}
        response = self.client.patch(self.detail_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.phone, "99999-0000")

    def test_delete_customer(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)