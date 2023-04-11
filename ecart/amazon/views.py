from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import Product,Cart

# Create your views here.
# @login_required
def home(request):
    return render(request, 'amazon/home.html')
def cart(request):
    return render(request, 'amazon/cart.html')


 

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            

            # print(username,password)

            return redirect('amazon:home')
             
    return render(request,'amazon/login.html')
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = Cart(user=request.user)
        cart.save()
    cart.products.add(product)
    cart.save()
    return redirect('cart')
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.filter(user=request.user).first()
    cart.products.remove(product)
    cart.save()
    return redirect('cart')
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = Cart(user=request.user)
        cart.save()
    products = cart.products.all()
    total_price = sum([product.price for product in products])
    context = {
        'products': products,
        'total_price': total_price
    }
    return render(request, 'amazon/cart.html', context)