from django.test import TestCase
from django.contrib.auth import get_user_model

from auction.models import Offer, Product


def sample_user(email='test@email.com', password='testpass'):
    '''
    Creates a sample user for tests.
    '''
    return get_user_model().objects.create_user(email=email, password=password)


class ModelTests(TestCase):

    def test_offer_str(self):
        '''
        Test the Offer model string representation.
        '''
        user = sample_user()
        product = Product.objects.create(
            user=user,
            name='Frozen yoghurt'
        )
        offer = Offer.objects.create(
            user=user,
            product=product,
            price='50',
            items_in_stock='10'
        )

        self.assertEqual(
            str(offer),
            '{}: ${} ({} in stock)'.format(
                product.name,
                offer.price,
                offer.items_in_stock
            )
        )

    def test_product_str(self):
        '''
        Test the Product model string representation.
        '''
        product = Product.objects.create(
            user=sample_user(),
            name='Frozen yoghurt'
        )

        self.assertEqual(str(product), product.name)
