from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list, name='products_list'),
    path('replenish/<int:count>/', views.replenish_products, name='replenish_products'),
]