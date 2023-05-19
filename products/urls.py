from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='products_index'),
   path('<int:product_id>', views.details, name='products_detail'),
]
