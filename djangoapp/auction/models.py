import requests
import json

from decimal import Decimal


from decouple import config

from django.db import models
from django.conf import settings

from django.db.models.signals import post_save, pre_save

from auction.signals import register_product


class Product(models.Model):
    '''
    Each product corresponds to a real world product you can buy.
    '''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    current_average_price = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2)
    price_percentage_change = models.DecimalField(
        default=0.00,
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return self.name


class Offer(models.Model):
    '''
    Each offer represents a product offer being sold for some price somewhere.
    '''
    product = models.ForeignKey(
        'Product',
        related_name='offers',
        on_delete=models.CASCADE
    )
    price = models.PositiveIntegerField()
    items_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return ('{}: ${} ({} in stock)'.format(
            self.product.name,
            self.price,
            self.items_in_stock
            )
        )


class Buffer(models.Model):
    value = models.DateTimeField()


def update_offers(sender, **kwargs):
    '''
    Updates all products with new offers
    '''
    for product in Product.objects.all():
        update_single_products_offers(product.id)


def update_single_products_offers(product_id):
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

        # Save the old average product price before deletion
        old_average_price = product.current_average_price

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

        # Calculating current average price and price percentage change
        # for the new requested product offers.
        new_offers = Offer.objects.filter(product=product)

        # Total number of offered items in all stocks
        offer_count = 0
        # Total price of all offers from all shops/stocks
        offer_total = 0
        for offer in new_offers:
            offer_count += offer.items_in_stock
            offer_total += (offer.price * offer.items_in_stock)

        new_average_price = Decimal(str(round(offer_total / offer_count, 2)))

        if (old_average_price == 0):
            if (new_average_price > 0):
                Product.objects.filter(id=product_id).update(
                    current_average_price=new_average_price,
                    price_percentage_change=Decimal('1.00')
                )
            elif (new_average_price < 0):
                Product.objects.filter(id=product_id).update(
                    current_average_price=new_average_price,
                    price_percentage_change=Decimal('-1.00')
                )
            else:
                Product.objects.filter(id=product_id).update(
                    current_average_price=Decimal('0.00'),
                    price_percentage_change=Decimal('0.00')
                )
        else:
            # Price percentage change
            ppc = (new_average_price - old_average_price) / old_average_price

            Product.objects.filter(id=product_id).update(
                current_average_price=new_average_price,
                price_percentage_change=Decimal(str(round(ppc, 2)))
            )


if not config('DEBUG'):
    post_save.connect(register_product, sender=Product)
else:
    pre_save.connect(update_offers, sender=Buffer)
