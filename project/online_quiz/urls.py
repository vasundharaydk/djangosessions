from django.urls import path
from . import views
app_name = "online_quiz"
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login',views.student_login,name='student_login'),
    path('signup',views.register_page,name='register_page')
]