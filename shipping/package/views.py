from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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
        username_ = request.POST.get('username','')
        password_ = request.POST.get('password','')
        user = authenticate(request, username=username_, password=password_)
        if user is not None:
            # if user.is_active:
                login(request, user)
                print(username_,password_)
                return redirect( 'package:postman')
        else:
            error_message = ' invalid user'
    return render(request, 'package/login.html',{'error_message':error_message})

@login_required(login_url='package:login_view')
def postman(request):
    package_details = Package.objects.all()
    
    return render(request, 'package/postman.html',{'package_details':package_details})
def logout_view(request):
    logout(request)
    return redirect( 'package:login_view')

@login_required(login_url='package:login_view')
def modify_package(request, id):
    package = Package.objects.get(id=id)
    newstatus = request.POST.get('status',package.status)
    neweta = request.POST.get('eta', package.eta)
    package.status = newstatus
    package.eta = neweta
    package.save()
    return redirect('package:postman')
def package_detail(request,id):
    package = Package.objects.get(id=id)
    return render(request, 'package/package_detail.html',{'package':package})

        
        