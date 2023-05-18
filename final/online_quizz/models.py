from django.db import models
from django.contrib.auth.models import Group

# Create your models here.
from django.contrib.auth.models import User

class Course(models.Model):
   course_name = models.CharField(max_length=50)
   description = models.CharField(max_length=200)
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return f'{self.course_name},{self.description}' 

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question_number = models.IntegerField(default=1)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):

    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    percentage = models.FloatField()


    def __str__(self):
        return f"Result for {self.exam.course_name}"