from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Manager


# Create your views here.
@login_required (login_url ='delivery_trucks:login_to_free_truck')
def home_page(request):
    return render(request ,'delivery_trucks/home.html')
def free_page(request):
    return render(request,'delivery_trucks/free.html')
    

def login_to_free_truck(request):
    error_message = ''
    if request.method == 'POST':
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        user = authenticate(username=username_, password=password_)
        if user is not None:
            login(request, user)
            manager = Manager.objects.get(user=user)
            return redirect('delivery_trucks:home_page')
        else:
            error_message = 'Wrong password'
    context = {'error_message': error_message}
    return render(request, 'delivery_trucks/login.html',)