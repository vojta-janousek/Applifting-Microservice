from django.db import models
from django.conf import settings


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

    def __str__(self):
        return self.name


class Offer(models.Model):
    '''
    Each offer represents a product offer being sold for some price somewhere.
    '''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    items_in_stock = models.PositiveIntegerField()
    found_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ('{}: ${} ({} in stock)'.format(
            self.product.name,
            self.price,
            self.items_in_stock
            )
        )
