from django.urls import path
from . import views
app_name = "online_quizz"
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login',views.student_login,name='student_login'),
    path('signup',views.register_page,name='register_page'),
    path('exam/',views.exam,name='exam'),
    path('question',views.questions,name='questions'),
    # path('list',views.course_list,name='course_list'),
    # path('details',views.course_detail,name='course_detail')
    path('courses/', views.course_list, name='course_list'),
    path('details/<int:pk>/', views.course_detail, name='course_detail'),
]