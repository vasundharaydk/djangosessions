from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'amazon/home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(username=username, password=password)

        print(username,password)
        if User is not None:
            login(request,User)
            return redirect(request,'amazon:home')
             
    return render(request,'amazon/login.html')
