from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User
from .models import Student,Teacher,Course,Question,Result

def home_page(request):
    return render(request,"online_quiz/main.html")

def student_login(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            # user_ = customer.objects.get(user=user)
            return redirect('online_quiz:home_page',)
            # print(username,password,user.id)
        else:
            error_message = 'Invalid login credentials'
    return render(request,'online_quiz/student_login.html',{'error_message':error_message})
def register_page(request): 
    if request.method == "POST":
        username_ = request.POST.get('username','')
        email_ = request.POST.get('email','')
        password_ = request.POST.get('password','')
        confirm_password_ = request.POST.get('confirm_password','')
        if password_ == confirm_password_:
            if len(Student.user.objects.filter(username = username_)) > 0:
                return redirect('online_quiz:register_page')
            else:
                if len(Student.objects.filter(email = email_)) > 0:
                    return redirect('online_quiz:register_page')
                else:
                    user = Student.objects.create_user(username = username_,email = email_)
                    user.set_password(password_)
                    user.save()
                    return redirect('online_quiz:home_page')   
    return render(request,'online_quiz/student_sign.html')