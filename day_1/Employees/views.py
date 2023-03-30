from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from . models import Employees,Attendance

def employee_details(request,id):
    employee_ = Employees.objects.get(id=id)
    attendance=Attendance.objects.filter(employees=employee_)


    # is_authenticated = request.session.get('logged_in_employees') == id
    # print(employee_.name)
    is_authenticated = request.session.get('logged_in_employees') == employee_.user.username
    context = {'employee': employee_, 'attendance': attendance}
    if is_authenticated:
        context['authenticated_employee_id'] = id
    return render(request, 'Employees/log.html', context)


   

def mark_attendance(request,id):
    employee_ = Employees.objects.get(id=id)
    date_ = request.POST.get('date')
    attendance_ =request.POST.get('attendance')
    log =Attendance(employees=employee_,date_field=date_,attendance=attendance_)
    log.save()
    return redirect('Employees:employee_details',employee_.id)


def login_to_session(request):
    error_message = ''
    if request.method == 'POST':
        # employee_id = request.POST.get('id')
        # password = request.POST.get('password')
        # employee_ = Employees.objects.get(pk=employee_id)

        # if password == employee_.password:
        #     request.session['logged_in_employee'] = employee_.id
        #     return redirect('Employees:employee_details', employee_id)
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        user = authenticate(username=username_, password=password_)
        if user is not None:
            request.session['logged_in_student'] = user.username
            employee_ = Employees.objects.get(user=user)
            return redirect('Employees:employee_details', employee_.id)

        else:
            error_message = 'Wrong password'
    context = {'error_message': error_message}
    return render(request, 'Employees/login.html', context)

def logout(request):
    del request.session['logged_in_employee']
    return redirect('Employees:login')
