from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.username}" 
class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20,null=False)
    email = models.CharField(max_length=200)
   
    def __str__(self):
         return f"{self.username}" 
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   description = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name , self.description

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)


# su: project
# p : project@123