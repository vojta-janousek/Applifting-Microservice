from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
ME_URL = reverse('user:me')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    '''
    Test the users API (public).
    '''

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success_check_status_code(self):
        '''
        Test creating user with valid payload is successful.
        #1 - Status code check
        '''
        payload = {
            'email': 'test@email.com',
            'password': 'testpass',
            'name': 'Test Name'
        }
        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_valid_user_success_check_password(self):
        '''
        Test creating user with valid payload is successful.
        #2 - Password check
        '''
        payload = {
            'email': 'test@email.com',
            'password': 'testpass',
            'name': 'Test Name'
        }
        response = self.client.post(CREATE_USER_URL, payload)
        user = get_user_model().objects.get(**response.data)

        self.assertTrue(user.check_password(payload['password']))

    def test_create_valid_user_success_password_hidden(self):
        '''
        Test creating user with valid payload is successful.
        #3 - Check that the password is hidden
        '''
        payload = {
            'email': 'test@email.com',
            'password': 'testpass',
            'name': 'Test Name'
        }
        response = self.client.post(CREATE_USER_URL, payload)

        self.assertNotIn('password', response.data)

    def test_user_exists(self):
        '''
        Tests that creating a user that already exists fails.
        '''
        payload = {
            'email': 'test@email.com',
            'password': 'testpass'
        }
        create_user(**payload)

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        '''
        Test that the password must be more than 5 characters long.
        '''
        payload = {
            'email': 'test@email.com',
            'password': 'py',
        }
        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user_exists = get_user_model().objects.filter(
            email=payload['email']
        )
        self.assertFalse(user_exists)

    def test_retrieve_user_unauthorized(self):
        '''
        Test that authentication is always required for users.
        '''
        response = self.client.get(ME_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateUserApiTests(TestCase):
    '''
    Test API requests that require authentication.
    '''

    def setUp(self):
        self.user = create_user(
            email='test@email.com',
            password='testpass',
            name='Test Name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        '''
        Test retrieving profile being possible.
        '''
        response = self.client.get(ME_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_profile(self):
        '''
        Test retrieving profile for logged in users.
        '''
        response = self.client.get(ME_URL)

        self.assertEqual(response.data, {
            'name': self.user.name,
            'email': self.user.email
        })

    def test_post_me_not_allowed(self):
        '''
        Test that post is not allowed on the me url.
        '''
        response = self.client.post(ME_URL, {})
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_update_user_profile_name_check(self):
        '''
        Test updating the user profile for authenticated user.
        #1 - Checks the name
        '''
        payload = {
            'name': 'New Name',
            'password': 'newpassword'
        }
        self.client.patch(ME_URL, payload)
        self.user.refresh_from_db()

        self.assertEqual(self.user.name, payload['name'])

    def test_update_user_profile_password_check(self):
        '''
        Test updating the user profile for authenticated user.
        #2 - Checks the password
        '''
        payload = {
            'name': 'New Name',
            'password': 'newpassword'
        }
        self.client.patch(ME_URL, payload)
        self.user.refresh_from_db()

        self.assertTrue(self.user.check_password(payload['password']))

    def test_update_user_profile_status_check(self):
        '''
        Test updating the user profile for authenticated user.
        #3 - Checks the status code
        '''
        payload = {
            'name': 'New Name',
            'password': 'newpassword'
        }
        response = self.client.patch(ME_URL, payload)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
