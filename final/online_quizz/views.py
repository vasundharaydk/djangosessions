from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User, Group
from .models import Student,Teacher,Course,Question,Result

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
            teacher = Group.objects.get(name='teacher')
            student = Group.objects.get(name='student')
            if teacher in user.groups.all():
                #redirect to teacher homepage
                return redirect()
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
# def move(request):
#     qs = Question.objects.all().order_by('pk')
#     q = qs[0]
#     prev = get_next_or_prev(qs, q, 'prev')
#     next = get_next_or_prev(qs, q, 'next')
def evaluate(request):
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=Question.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/questions.html',context)

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'online_quizz/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'online_quizz/course_detail.html', {'course': course})
