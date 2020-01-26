import requests
import json

from unittest import TestCase


class ProductRequestTests(TestCase):
    '''
    These would be tested in random order, which would not have worked.
    As a result, they have all been conglomerated into a single test method.
    '''

    def setUp(self):
        self.domain = 'http://localhost:8000'

        # Product objects
        self.app_endpoint = '/api/auction/'
        self.request_endpoint = 'product/'
        self.url = self.domain + self.app_endpoint + self.request_endpoint

        self.data = {
            'name': 'Frozen yoghurt',
            'description': 'A cold snack'
        }

        self.auth = ('goulash.elemer@email.com', 'goulashelemer')

        self.product_id = 0

    def test_create_new_product(self):
        '''
        Test creating a new product using requests.
        '''
        product_create_request = requests.post(
                                        url=self.url,
                                        data=self.data,
                                        auth=self.auth
                                        )
        self.product_id = (json.loads(product_create_request.text))['id']
        self.assertEqual(product_create_request.status_code, 201)

    # def test_retrieving_existing_product(self):
        '''
        Test retrieving an existing product using requests.
        '''
        self.url = self.url + str(self.product_id) + '/'
        product_get_request = requests.get(url=self.url, auth=self.auth)
        get_data = json.loads(product_get_request.text)

        self.assertEqual(product_get_request.status_code, 200)
        self.assertEqual(get_data['name'], self.data['name'])
        self.assertEqual(get_data['description'], self.data['description'])

    # def test_updating_existing_product(self):
        '''
        Test updating an existing product using requests.
        '''
        new_data = {
            'name': 'Hummus dip',
            'description': 'It might kill you'
        }
        product_put_request = requests.put(
                                        url=self.url,
                                        data=new_data,
                                        auth=self.auth
                                        )
        put_data = json.loads(product_put_request.text)

        self.assertEqual(product_put_request.status_code, 200)
        self.assertEqual(put_data['name'], new_data['name'])
        self.assertEqual(put_data['description'], new_data['description'])
