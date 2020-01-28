from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from auction.models import Product, Offer
from auction.serializers import ProductSerializer, ProductDetailSerializer


PRODUCTS_URL = reverse('auction:product-list')


def detail_url(product_id):
    '''
    Returns product detail URL.
    '''
    return reverse('auction:product-detail', args=[product_id])


def sample_product(user, name='Frozen yoghurt'):
    '''
    Creates and returns a sample product.
    '''
    return Product.objects.create(user=user, name=name)


class PublicProductAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        '''
        Test that login is required for retrieving products.
        '''
        response = self.client.get(PRODUCTS_URL)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateProductAPITests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@email.com',
            password='testpass'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_products_status(self):
        '''
        Test retrieving products by an authenticated user.
        '''
        Product.objects.create(user=self.user, name='Frozen yoghurt')
        Product.objects.create(user=self.user, name='Hummus dip')

        response = self.client.get(PRODUCTS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_products_data(self):
        '''
        Test retrieving products by an authenticated user.
        '''
        Product.objects.create(user=self.user, name='Frozen yoghurt')
        Product.objects.create(user=self.user, name='Hummus dip')

        response = self.client.get(PRODUCTS_URL)
        products = Product.objects.all().order_by('id')
        serializer = ProductSerializer(products, many=True)

        self.assertEqual(response.data, serializer.data)

    def test_products_limited_to_user_status(self):
        '''
        Test that tags returned are for the authenticated user only.
        '''
        user2 = get_user_model().objects.create_user(
            email='test2@email.com',
            password='testpass2'
        )
        Product.objects.create(user=user2, name='Frozen yoghurt')

        response = self.client.get(PRODUCTS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_products_limited_to_user_count(self):
        '''
        Test that tags returned are for the authenticated user only.
        '''
        user2 = get_user_model().objects.create_user(
            email='test2@email.com',
            password='testpass2'
        )
        Product.objects.create(user=user2, name='Frozen yoghurt')
        Product.objects.create(user=self.user, name='Hummus dip')
        response = self.client.get(PRODUCTS_URL)

        self.assertEqual(len(response.data), 1)

    def test_products_limited_to_user_data(self):
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

        self.assertEqual(response.data[0]['name'], product.name)

    def test_create_product_successful(self):
        '''
        Test creating a new product.
        '''
        payload = {'name': 'Frozen yoghurt', 'description': 'not bad'}
        self.client.post(PRODUCTS_URL, payload)

        product = Product.objects.filter(
            user=self.user,
            name=payload['name']
        )
        exists = product.exists()

        self.assertTrue(exists)

    def test_create_product_invalid(self):
        '''
        Test creating a new product with an invalid payload.
        '''
        payload = {'name': ''}
        response = self.client.post(PRODUCTS_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProductDetailAPITests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@email.com',
            password='testpass'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_view_product_detail(self):
        '''
        Test viewing a product detail.
        '''
        product = sample_product(user=self.user)
        Offer.objects.create(
            product=product,
            price=10,
            items_in_stock=2
        )

        url = detail_url(product.id)
        response = self.client.get(url)
        serializer = ProductDetailSerializer(product)

        self.assertEqual(response.data, serializer.data)
