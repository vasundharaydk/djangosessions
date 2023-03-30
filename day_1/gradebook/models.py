# from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 256)

    def __str__(self):
        return f' {self.name}'

class Marks(models.Model):
    subject_name = models.CharField(max_length = 128)
    score = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #having a list of Marks inside every student
    #is the same as having a student inside every Mark

    def __str__(self):
        return f'{self.student} - {self.subject_name} - {self.score}'