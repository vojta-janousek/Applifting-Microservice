from django.db import models


class Product(models.Model):
    '''
    Each product corresponds to a real world product you can buy.
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Offer(models.Model):
    '''
    Each offer represents a product offer being sold for some price somewhere.
    '''
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    items_in_stock = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.price)
