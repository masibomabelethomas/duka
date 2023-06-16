from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, NewArrival
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})

# @login_required
def home(request):
    return render(request, 'home.html')

# def detail(request, product_id):
#     return HttpResponse(product_id)
    

# def Newarrival_views(request):
#     newarrival = Newarrival.objects.all()
#     return render(request, 'index.html', {'products':products})
 

# def Offers_views(request):
#     offers = Offers.objects.all()
 