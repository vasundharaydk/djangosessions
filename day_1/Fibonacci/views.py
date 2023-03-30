from django.shortcuts import render
from django.http import HttpResponse
from .Fibonacci import Fibonacci_series

# Create your views here.
def get_Fibonacci_sequence(request,start):
    sequence = Fibonacci_series(start)
    standard_response = f'''
    <!DOCTYPE html>
        <html>
            <head>
            <title>Fibonacci Sequence</title>
            </head>
            <body>
                <h2 style="text-align:center;">Fibonacci sequence for {start} is: </h2>
                <p style="text-align:center;">{sequence}</p>
            </body>
        </html>
    
    
    '''
    return HttpResponse(standard_response)

def get_Fibonacci_req_params(request):
    start = int(request.GET.get('start','10'))
    sequence = Fibonacci_series(start)
    standard_response = f'''
    <!DOCTYPE html>
        <html>
            <head>
            <title>Fibonacci Sequence</title>
            </head>
            <body>
                <h2 style="text-align:center;">Fibonacci sequence for {start} is: </h2>
                <pstyle="text-align:center;">{sequence}</p>
            </body>
        </html>
    
    
    '''
    return HttpResponse(standard_response)

def process_fibonacci_form(request):
    start = int(request.POST.get('start','10'))
    sequence = Fibonacci_series(start)
    standard_response = f'''
     <!DOCTYPE html>
        <html>
            <head>
            <title>Fibonacci Sequence</title>
            </head>
            <body>
                <h2 style="text-align:center;">Fibonacci sequence for {start} is: </h2>
                <p style="text-align:center;">{sequence}</p>
            </body>
        </html>
    

    '''
    return HttpResponse(standard_response)
def show_Fibonacci_form(request):
    return render(request,'Fibonacci/Fibonacci.html')
