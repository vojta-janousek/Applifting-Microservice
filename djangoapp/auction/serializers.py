from rest_framework import serializers

from auction.models import Product, Offer


class OfferSerializer(serializers.ModelSerializer):
    '''
    A serializer for offer object list.
    '''

    class Meta:
        model = Offer
        fields = ('id', 'price', 'items_in_stock', 'found_at')
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    '''
    A serializer for product object list.
    '''

    offers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'offers',)
        read_only_fields = ('id',)


class ProductDetailSerializer(ProductSerializer):
    '''
    A serializer for product object details.
    '''
    offers = OfferSerializer(many=True, read_only=True)
