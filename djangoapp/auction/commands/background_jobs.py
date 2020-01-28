import requests
import json

from decouple import config

from auction.models import Product, Offer


def update_product_offers(product_id):
    '''
    Pulls new offers for a product from the Offers microservice,
    then updates the offers in the database.
    '''
    base_url = config('OFFERS_URL')
    offers_url = base_url + '/products/{}/offers'.format(str(product_id))

    token = config('ACCESS_TOKEN')
    headers = {
        'Bearer': token
    }

    # Fetches fresh offers for a given product from the Offers microservice
    offers_request = requests.get(url=offers_url, headers=headers)

    if (offers_request.status_code == 200):
        product = (Product.objects.filter(id=product_id))[0]

        # Deletes all offers of a product whose product_id was given
        Offer.objects.filter(product=product).delete()

        # Repopulates the product with new offers fetched from the Offers MS
        data = json.loads(offers_request.text)
        for offer in data:
            Offer.objects.create(
                product=product,
                price=offer['price'],
                items_in_stock=offer['items_in_stock']
            )


if (__name__ == '__main__'):
    # For testing purposes
    id = 1
    print(update_product_offers(id))
