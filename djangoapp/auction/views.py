from django.views.generic import TemplateView

from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from auction.models import Product, Buffer
from auction.serializers import (ProductSerializer, ProductDetailSerializer,
                                 BufferSerializer)
from auction.tasks import update_all_products


class IndexView(TemplateView):
    template_name = 'auction/index.html'


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


class BufferDetailAPIView(APIView):

    def get_object(self, pk):
        buffer = get_object_or_404(Buffer, pk=pk)
        return buffer

    def get(self, request, pk):
        buffer = self.get_object(pk)
        serializer = BufferSerializer(buffer)
        return Response(serializer.data)

    def put(self, request, pk):
        buffer = self.get_object(pk)
        serializer = BufferSerializer(buffer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            update_all_products(schedule=5, repeat=60)
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
