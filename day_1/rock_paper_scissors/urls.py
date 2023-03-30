from django.urls import path
from . import  views
urlpatterns = [
    path('start',views.game_view,name='game_view'), 
    
 ]