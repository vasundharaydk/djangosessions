from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:id>',views.notice_board,name='notice_board')
    ]