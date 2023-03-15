from django.urls import path
from .views import index, products

urlpatterns = [
    path('', index, name='main'),
    path('products/', products, name='products'),
]
