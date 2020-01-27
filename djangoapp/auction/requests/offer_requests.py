import requests
import json

from unittest import TestCase


class OfferRequestTests(TestCase):
    '''

    '''

    def setUp(self):
        self.domain = 'http://localhost:8000'

        # Product objects
        self.app_endpoint = '/api/auction/'
        self.request_endpoint = 'product/'
        self.url = self.domain + self.app_endpoint + self.request_endpoint

        self.auth = ('goulash.elemer@email.com', 'goulashelemer')

        data = {
            'name': 'Frozen yoghurt',
            'description': 'A cold snack'
        }
        product_create_request = requests.post(
                                        url=self.url,
                                        data=data,
                                        auth=self.auth
                                        )
        self.product_id = (json.loads(product_create_request.text))['id']

    def test_create_new_offer(self):
        '''
        Test creating a new offer using requests.
        '''
        url = self.url + str(self.product_id) + '/'
        data = {
            'service_id': 1,
            'price': 50,
            'items_in_stock': 4
        }
        offer_create_request = requests.post(
            url=url,
            data=data,
            auth=self.auth
        )

        self.assertEqual(offer_create_request.status_code, 405)
