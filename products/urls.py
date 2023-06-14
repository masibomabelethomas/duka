from django.urls import path, include
from . import views
from api.models import ProductResource

product_resource = ProductResource()
urlpatterns = [
   path('', views.home, name='home'),
   path('products/', views.products, name='products'),
   path('api/', include(product_resource.urls)),
   # path('login/', views.login_user, name='login'),
   # path('<int:product_id>', views.details, name='products_detail'),
]
