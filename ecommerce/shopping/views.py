from django.shortcuts import render,redirect
from .models import product_data,customer,cart
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request,'shopping/home.html')
def product_data_(request):
    
        product_details =product_data.objects.all()
        context = {'product':product_details}
        return render(request,'shopping/home.html',context)
  

def add_to_cart(request,name):
    full_name_ =request.session.get('full_name')
    user_object = customer.objects.get(full_name =full_name_)
    product_data_object =product_data.objects.get(name= name)
    cart_items = {item.product_id.name : item for item in cart.objects.filter(customer =user_object)}
    if name in cart_items:
        cart_items[name].quantity +=1
        cart_items[name].save()
                
    else:
        cart_ = cart(customer=user_object,product_id=product_data_object)
        cart_.save()
    
    return redirect('shopping:product_data')
    # else:
    #     error_message = "please login"
    #     context = {'error_message': error_message}
    #     return render(request,'shopping/cart.html',context)
def cart_data(request):
    # if request.session.get('acccess'):
        full_name_ = request.session.get('full_name')
        user_object =customer.objects.get(full_name = full_name_)
        cart_data = cart.objects.filter(customer =user_object)
        cart_total = sum([c.product_id.price * c.quantity for c in cart.objects.filter()])
        context ={'products':cart_data,'cart_total':cart_total}
        return render(request,'shopping/cart.html',context)
    # return redirect('shopping:login')

def login(request):
    error_message = ''
    if request.method == 'POST':
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        user = authenticate(username=username_,password=password_)

        
        if user is not None:
            user_objects =customer.objects.filter(user =user)
            print(user_objects)
            if (len(user_objects) == 0):
                error_message = "No customer object associated with this login id"
                return render(request, 'shopping/login.html', {'error_message': error_message})
            request.session['full_name'] = user_objects[0].full_name
            request.session['access'] = True
            return redirect('shopping:product_data')
        else:
            error_message = "Invalid login credentials"
            
    return render(request,'shopping/login.html', {'error_message': error_message})

def logout(request):
    del request.session['full_name']
    del request.session['access']
    return redirect('shopping:login')
