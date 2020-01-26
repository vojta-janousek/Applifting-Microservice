import requests

from unittest import TestCase


class UserRequestTests(TestCase):

    def setUp(self):
        self.domain = 'http://localhost:8000'

        # User objects
        self.app_endpoint = '/api/user/'
        self.request_endpoint = 'create/'
        self.url = self.domain + self.app_endpoint + self.request_endpoint

        # Enter new user's credentials
        self.data = {
            'email': 'goulash.elemer@email.com',
            'password': 'goulashelemer',
            'name': 'Goulash Elemer'
        }

    def test_create_new_user(self):
        '''
        Test creating a new user with requests.
        '''
        user_create_request = requests.post(self.url, self.data)
        self.assertEqual(user_create_request.status_code, 201)

        same_create_request = requests.post(self.url, self.data)
        self.assertEqual(same_create_request.status_code, 400)

    # def test_create_existing_user_fail(self):
    #     '''
    #     Test that creating an already existing user fails.
    #     '''
    #     user_create_request = requests.post(self.url, self.data)
    #
    #     self.assertEqual(user_create_request.status_code, 400)
