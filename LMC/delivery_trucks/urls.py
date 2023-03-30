from django.urls import path
from . import views

app_name ='delivery_trucks'

urlpatterns =[
    path('home',views.home_page,name='home_page'),
    path('free_trucks',views.login_to_free_truck,name='login_to_free_truck'),
]