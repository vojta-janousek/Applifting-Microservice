from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from auction.models import Product
from auction.serializers import ProductSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    Manage products in the database.
    '''
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    def get_queryset(self):
        '''
        Return the products to the authenticated user.
        '''
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        '''
        Return appropriate serializer class.
        '''
        if self.action == 'retrieve':
            return ProductDetailSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        '''
        Create a new product.
        '''
        serializer.save(user=self.request.user)

# class ProductViewSet(viewsets.GenericViewSet,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin):
#     '''
#     Manage products in the database.
#     '''
#     # authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user).order_by('id')
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
