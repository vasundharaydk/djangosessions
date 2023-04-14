from django.urls import path
from . import views

app_name = 'shipping_app'

urlpatterns =[
    path('home',views.register,name='register'),
    path('login',views.login_view,name='login_view')
]
