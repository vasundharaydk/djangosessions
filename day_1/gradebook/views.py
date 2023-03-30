# from django.shortcuts import render,redirect
# from .models import Student,Marks
# # Create your views here.

# def student_details(request,id):#read
#     student_=Student.objects.get(pk=id)
#     marks = Marks.objects.filter(student=student_)
#     context ={'student':student_,'marks':marks}
#     return render(request,'gradebook/marksheet.html',context)
# def add_marks(request,id): #create
#     student_ = Student.objects.get(pk=id)
#     sub_name = request.POST.get('sub_name')
#     score_ =request.POST.get('score')

#     marks =Marks(student=student_,subject_name=sub_name,score=score_)
#     marks.save()
#     return redirect('gradebook:student_details',student_.id)
# def delete_marks(request, id):
#     #this is the Delete of crud
#     marks = Marks.objects.get(pk=id)
#     marks.delete()
#     return redirect('gradebook:student_details', marks.student.id)
from django.shortcuts import render, redirect
from .models import Student, Marks
from django.http  import HttpResponse
# Create your views here.

def new_student(request,name_):
    student=Student(name=name_)
    student.save()
    return HttpResponse('ok')
    

def student_detail(request, id):
    #this is the R of CRUD
    student_ = Student.objects.get(pk=id)
    #SELECT * FROM STUDENT WHERE <INSERT PRIMARY KEY HERE>=id
    marks = Marks.objects.filter(student=student_)
    #SELECT * FROM MARKS WHERE STUDENT=(SELECT * FROM STUDENT
    # WHERE <INSERT PRIMARY KEY HERE>=id)

    context = {'student': student_, 'marks': marks}
    return render(request, 'gradebook\marksheet.html', context)

def add_marks(request, id):
    #this is the C of CRUD
    student_ = Student.objects.get(pk=id)

    sub_name_ = request.POST.get('sub_name')
    score_ = request.POST.get('score')

    marks = Marks(student=student_, subject_name=sub_name_, score=score_)
    marks.save()
    return redirect('gradebook:student_detail', student_.id)

def delete_marks(request, id):
    #this is the D of crud
    marks = Marks.objects.get(pk=id)
    marks.delete()
    return redirect('gradebook:student_detail', marks.student.id)
def update_marks(request,id):
    student_ =Student.objects.get(pk=id)
    marks = Marks.objects.filter(student=student_)

    name = request.POST.get('name')
    update_name = request.POST.get('update_name')
    update_score = request.POST.get('update_score')
    for item in marks:
        if item.subject_name == name:
            item.subject_name = update_name
            item.score = update_score
            item.save()
    return redirect('gradebook:student_detail', student_.id)
    # return HttpResponse(f'{marks[]}')
    

    # marks.update()

    #user = harish,user@2428


