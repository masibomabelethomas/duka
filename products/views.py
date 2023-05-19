from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, NewArrival
# Offer, 
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products':products})

# def detail(request, product_id):
#     return HttpResponse(product_id)
    

# def Newarrival_views(request):
#     newarrival = Newarrival.objects.all()
#     return render(request, 'index.html', {'products':products})
 

# def Offers_views(request):
#     offers = Offers.objects.all()
 