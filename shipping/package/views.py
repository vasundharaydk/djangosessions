from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . models import Package
# Create your views here.
def register_package(request):
    if request.method == 'GET':
        access = False
        return render(request, 'package/register_package.html')
    if request.method =='POST':
        access = True
        address_ = request.POST.get('address','')
        phone_ = request.POST.get('phone','')
        package = Package(address=address_,phone=phone_)
        package.save()
        package_id = package.id
        return render(request, 'package/register_package.html',{'package_id':package_id,'access':access})
        # return render(request, 'package/register_package.html')
def login_view(request):
    error_message = ''
    if request.method == 'GET':
        return render(request, 'package/login.html')
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(request, 'package:postman')
        else:
            error_message = ' invalid user'
    return render(request, 'package/login.html',{'error_message':error_message})
def postman(request):
    package_details = Package.objects.all()
    
    return render(request, 'package/postman.html',{'package_details':package_details})
def logout(request):
    logout(request)
    return redirect(request, 'package:login')

        
        