from django.urls import path
from . import views
app_name = "online_quizz"
urlpatterns = [
    path('home', views.home_page, name='home_page'),
    path('login',views.student_login,name='student_login'),
    path('signup',views.register_page,name='register_page'),
    path('courses/', views.course_list, name='course_list'),
    path('details/<int:pk>/', views.course_detail, name='course_detail'),
    path('evaluate/<int:course_id>/', views.evaluate_results, name='evaluate_results'),
    path('logout', views.logout_, name='logout'),
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('profile/', views.view_profile, name='profile'),
    path('teacher-view/', views.teacher_view, name='teacher_view'),
    path('teacher/courses/', views.teacher_courses, name='teacher_courses'),
    path('teacher/course/<int:course_id>/', views.course_details, name='course_details'),
    path('teacher/course/add/', views.add_course, name='add_course'),
    path('teacher/course/update/<int:course_id>/', views.update_course, name='update_course'),
    path('teacher/course/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('teacher/course/<int:course_id>/question/add/', views.add_question, name='add_question'),
    path('teacher/course/<int:course_id>/question/delete/<int:question_id>/', views.delete_question, name='delete_question'),
   
]