from django.urls import path
from . import views
app_name = 'package'
urlpatterns = [
    # path('', views.index, name='index'),
    path('register', views.register_package, name='register_package'),
    path('login',views.login_view,name='login_view'),
    path('postman',views.postman,name='postman')
]