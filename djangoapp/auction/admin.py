from django.contrib import admin

from auction.models import Offer, Product, Buffer


admin.site.register(Offer)
admin.site.register(Product)
admin.site.register(Buffer)
