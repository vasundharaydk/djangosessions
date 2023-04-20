from django.urls import path
from . import views
urlpatterns =[
    path('', views.home , name='home'),
    path('playgame',views.play_game ,name='play_game'),
]