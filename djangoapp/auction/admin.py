from django.contrib import admin

from auction.models import Offer, Product


admin.site.register(Offer)
admin.site.register(Product)
