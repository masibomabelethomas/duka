from django.contrib import admin
from .models import Product, NewArrival
#Offer

# from .models import NewArrivals
# from .models import Offer..
# Register your models here..

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
admin.site.register(Product, ProductAdmin)

class NewArrivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand','availability', 'arrival_date')
admin.site.register(NewArrival, NewArrivalAdmin)


# class OfferAdmin(admin.ModelAdmin):
#     list_display = ('code', 'description', 'discount')
# admin.site.register(Offer, OfferAdmin)
