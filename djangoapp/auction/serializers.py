from rest_framework import serializers

from auction.models import Product, Offer


class ProductSerializer(serializers.ModelSerializer):
    '''
    A serializer for product objects.
    '''
    class Meta:
        model = Product
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)


class OfferSerializer(serializers.ModelSerializer):
    '''
    A serializer for offer objects.
    '''
    pass
