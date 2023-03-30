from django.urls import path,include
from . import views

app_name = "Employees"
urlpatterns =[
    path('<int:id>',views.employee_details, name='employee_details'),
    path('employee/<int:id>',views.mark_attendance, name='mark_attendance'),
    path('login', views.login_to_session, name='login'),
    path('logout', views.logout, name='logout')
]