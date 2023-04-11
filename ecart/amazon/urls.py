from django.urls import path
from . import views

app_name='amazon'
urlpatterns =[
    path('',views.home,name='home'),
    path('cart',views.cart,name='cart'),
    path('login/',views.login_user,name='login_user')
]