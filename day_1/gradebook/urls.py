from django.urls import path
from . import views

app_name='gradebook'

urlpatterns = [
    path('student/add/<str:name_>',views.new_student,name='new_student'),
    path('student/<int:id>', views.student_detail, name='student_detail'),
    path('student/<int:id>/add', views.add_marks, name='add_marks'),
    path('student/<int:id>/delete', views.delete_marks, name='delete_marks'),
    path('student/update/<int:id>', views.update_marks, name='update_marks')

]