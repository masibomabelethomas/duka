from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from api.models import ProductResource
product_resource = ProductResource()

# @login_required

urlpatterns = [
   path('', views.home, name='home'),
   path('products/', views.products, name='products'),
   path('api/', include(product_resource.urls)),
   # path('login/', views.login_user, name='login'),
   # path('<int:product_id>', views.details, name='products_detail'),
]
