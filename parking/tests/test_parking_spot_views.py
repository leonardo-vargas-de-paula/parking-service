from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import ParkingSpot

class ParkingSpotAPITest(APITestCase):
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin_test',
            password='password123',
            email='admin@parking.com'
        )
        
        refresh = RefreshToken.for_user(self.admin_user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
        self.parking_spot_data = {
            "spot_number": "001",
            "is_occupied": False
        }


        self.parking_spot = ParkingSpot.objects.create(spot_number="002", is_occupied=False)
        self.list_url = reverse('parking-spot-list-create')
        self.detail_url = reverse('parking-spot-detail', kwargs={'pk': self.parking_spot.pk})

        
    def test_create_parking_spot_success(self):
        response = self.client.post(self.list_url, self.parking_spot_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['spot_number'], self.parking_spot_data['spot_number'])

    def test_create_parking_spot_missing_required_field(self):
        data = {"is_occupied": False} 
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('spot_number', response.data)

    def test_list_parking_spots(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
    
    def test_update_parking_spot(self):
        payload = {
            "spot_number": "001", #mantem
            "is_occupied": True
            }
        response = self.client.put(self.detail_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.parking_spot.refresh_from_db()
        self.assertEqual(self.parking_spot.is_occupied, True)

    def test_delete_parking_spot(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ParkingSpot.objects.count(), 0)
    