from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Student,Teacher,Course,Question,Result
from django.utils import timezone

def home_page(request):
    return render(request,"online_quizz/main.html")

def student_login(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            # user_ = customer.objects.get(user=user)
            teacher = Group.objects.get(name='teachers')
            student = Group.objects.get(name='students')
            if teacher in user.groups.all():
                #redirect to teacher homepage
                return redirect('online_quizz:teacher_dasboard')
            if student in user.groups.all():
                #redirect to student homepage
                return  redirect('online_quizz:course_list')
            return redirect('online_quizz:home_page',)
            # print(username,password,user.id)
        else:
            error_message = 'Invalid login credentials'
    return render(request,'online_quizz/student_login.html',{'error_message':error_message})
def register_page(request): 
    if request.method == "POST":
        username_ = request.POST.get('username','')
        email_ = request.POST.get('email','')
        password_ = request.POST.get('password','')
        confirm_password_ = request.POST.get('confirm_password','')
        if password_ == confirm_password_:
            if len(User.objects.filter(username = username_)) > 0:
                return redirect('online_quizz:register_page')
            else:
                if len(User.objects.filter(email = email_)) > 0:
                    return redirect('online_quizz:register_page')
                else:
                    user = User.objects.create_user(username = username_,email = email_)
                    user.set_password(password_)
                    user.save()
                    return redirect('online_quizz:home_page')   
    return render(request,'online_quizz/student_sign.html')
def exam(request):
    courses =Course.objects.all()
    for course in courses:
        questions = Question.objects.filter(course=course)
        course.questions = questions

    return render(request,'online_quizz/exam.html',{'courses':courses})
def questions(request):
    questions_ =Question.objects.all()
    return render(request,'online_quizz/questions.html',{'questions':questions_})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'online_quizz/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    questions = Question.objects.filter(course=course)
    return render(request, 'online_quizz/course_detail.html', {'course': course, 'questions': questions})
@login_required
def exam_results(request):
    courses = Course.objects.all()
    results = []
    for course in courses:
        exam_results = Result.objects.filter(student=request.student, exam=course)
        if exam_results:
            total_marks = course.total_marks
            obtained_marks = sum(result.marks for result in exam_results)
            percentage = obtained_marks / total_marks * 100
            results.append({
                'course': course,
                'obtained_marks': obtained_marks,
                'total_marks': total_marks,
                'percentage': percentage,
            })
    return render(request, 'online_quizz/exam_results.html', {'results': results})

