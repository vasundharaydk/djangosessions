from django.urls import path
from . import views

app_name='shopping'
urlpatterns=[
    path('home',views.home,name='home'),
    path('product_data',views.product_data_ ,name ='product_data'),
    path('login',views.login,name='login'),
    path('cart_data',views.cart_data,name='cart_data'),
    path('add_to_cart/<str:name>',views.add_to_cart,name='add_to_cart'),
    path('logout',views.logout,name='logout'),
]