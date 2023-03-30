from django.urls import path
from . import views

app_name='amazon'
urlpatterns =[
    path('home/',views.home,name='home'),
    path('login/',views.login_user,name='login_user')
]