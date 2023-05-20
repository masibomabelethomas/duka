from django.urls import path
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('products/', views.products, name='products'),
   # path('<int:product_id>', views.details, name='products_detail'),
]
