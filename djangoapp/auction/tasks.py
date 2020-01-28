from __future__ import absolute_import, unicode_literals

from celery import shared_task

from auction.models import Product
from auction.commands.background_jobs import update_product_offers


@shared_task(name='summary')
def background_product_offers_update():
    '''
    A periodic call to a function updating all offers of all products
    currently in the database.
    '''
    for product in Product.objects.all():
        update_product_offers(product.id)
