from django.urls import path, include
from rest_framework.routers import DefaultRouter

from auction.views import ProductViewSet

# Router automatically generates URLs for view sets
# All actions of a view set are appropriately assigned a URL
router = DefaultRouter()
router.register('product', ProductViewSet)

app_name = 'auction'

urlpatterns = [
    path('', include(router.urls)),
]
