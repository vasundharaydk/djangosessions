from django.urls import path
from . import views

urlpatterns =[
    path('<int:start>', views.get_Fibonacci_sequence, name='fibonacci_sequence'),
    path('withparams', views.get_Fibonacci_req_params, name='fibonnaci_withparams'),
    path('processform',views.process_fibonacci_form,name='process_fibonacci_form'),
    path('form',views.show_Fibonacci_form, name='show_collatz_form')

]