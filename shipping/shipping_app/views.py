from django.shortcuts import render,redirect
from . models import  Customer,Postman
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def register(request):
    details=''
    if request.method == 'POST':
        address_ = request.POST.get('address')
        phone_number_ =request.POST.get('phone_number')
        register_ = Customer(address=address_,phone_number=phone_number_)
        register_.save()
        details = {item.package_id : item for item in Customer.objects.filter(customer =register_)}
    return render(request,'shipping_app/home.html')


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        user = authenticate(username=username_,password=password_)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('shipping_app/modifypage.html')
        else:
            error_message = 'Invalid username or password'
            return render('shopping_app/login.html',{'error_message':error_message})
    return redirect('shipping_app:login')

