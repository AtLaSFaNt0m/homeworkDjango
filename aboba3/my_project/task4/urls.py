from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='home'),
    path('shop/', views.shop_view, name='shop'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<str:game_name>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout'),  # Добавьте эту строку
]
