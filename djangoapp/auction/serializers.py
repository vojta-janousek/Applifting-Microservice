from rest_framework import serializers

from auction.models import Product, Offer, Buffer


class OfferSerializer(serializers.ModelSerializer):
    '''
    A serializer for offer object list.
    '''

    class Meta:
        model = Offer
        fields = ('id', 'price', 'items_in_stock')
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    '''
    A serializer for product object list.
    '''

    offers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'current_average_price',
            'price_percentage_change',
            'offers'
        )
        read_only_fields = (
            'id',
            'current_average_price',
            'price_percentage_change'
        )


class ProductDetailSerializer(ProductSerializer):
    '''
    A serializer for product object details.
    '''
    offers = OfferSerializer(many=True, read_only=True)


class BufferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buffer
        fields = ('value',)
