from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from auction.models import Product
from auction.serializers import ProductSerializer


PRODUCTS_URL = reverse('auction:product-list')


class PublicProductAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        '''
        Test that login is required for retrieving products.
        '''
        response = self.client.get(PRODUCTS_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProductAPITests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@email.com',
            password='testpass'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_products(self):
        '''
        Test retrieving products by an authenticated user.
        '''
        Product.objects.create(user=self.user, name='Frozen yoghurt')
        Product.objects.create(user=self.user, name='Hummus dip')

        response = self.client.get(PRODUCTS_URL)
        products = Product.objects.all().order_by('-name')
        serializer = ProductSerializer(products, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_products_limited_to_user(self):
        '''
        Test that tags returned are for the authenticated user only.
        '''
        user2 = get_user_model().objects.create_user(
            email='test2@email.com',
            password='testpass2'
        )
        Product.objects.create(user=user2, name='Frozen yoghurt')
        product = Product.objects.create(user=self.user, name='Hummus dip')

        response = self.client.get(PRODUCTS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], product.name)

    def test_create_product_successful(self):
        '''
        Test creating a new product.
        '''
        payload = {'name': 'Frozen yoghurt', 'description': 'not bad'}
        response = self.client.post(PRODUCTS_URL, payload)

        product = Product.objects.filter(
            user=self.user,
            name=payload['name']
        )
        exists = product.exists()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_create_product_invalid(self):
        '''
        Test creating a new product with an invalid payload.
        '''
        payload = {'name': ''}
        response = self.client.post(PRODUCTS_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
