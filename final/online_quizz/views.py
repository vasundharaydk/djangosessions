from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.decorators import login_required ,permission_required
from django.contrib.auth.models import User, Group
from .models import Course,Question,Result


def home_page(request):
    return render(request,"online_quizz/main.html")

def student_login(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            # user_ = customer.objects.get(user=user)
            teacher = Group.objects.get(name='teachers')
            student = Group.objects.get(name='students')
            if teacher in user.groups.all():
                #redirect to teacher homepage
                return redirect('online_quizz:teacher_dashboard')
            if student in user.groups.all():
                #redirect to student homepage
                return  redirect('online_quizz:course_list')
            return redirect('online_quizz:home_page',)
            # print(username,password,user.id)
        else:
            error_message = 'Invalid login credentials'
    return render(request,'online_quizz/student_login.html',{'error_message':error_message})
def register_page(request): 
    error_message = ''
    if request.method == "POST":
        username_ = request.POST.get('username','')
        email_ = request.POST.get('email','')
        password_ = request.POST.get('password','')
        confirm_password_ = request.POST.get('confirm_password','')
        if password_ == confirm_password_:
            if len(User.objects.filter(username=username_)) > 0:
                return redirect('online_quizz:register_page')
            else:
                if len(User.objects.filter(email=email_)) > 0:
                    return redirect('online_quizz:register_page')
                else:
                    user = User.objects.create_user(username=username_, email=email_)
                    user.set_password(password_)
                    user.save()
                    error_message = 'Registration successful! You can now log in.'
                    return redirect('online_quizz:home_page')
        else:
            error_message = 'Password and confirm password do not match.'
      
    return render(request, 'online_quizz/student_sign.html',  {'error_message': error_message})

@permission_required('online_quizz.view_course',login_url='online_quizz:student_login')
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'online_quizz/course_list.html', {'courses': courses})

@permission_required('online_quizz.view_question',login_url='online_quizz:student_login')
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    questions = Question.objects.filter(course=course)
    return render(request, 'online_quizz/course_detail.html', {'course': course, 'questions': questions})

@permission_required('online_quizz.view_question',login_url='online_quizz:student_login')
def evaluate_results(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id)
        student_group = request.user.groups.first()
        student_answers = request.POST
        total_marks = 0
        obtained_marks = 0

        for question in course.question_set.all():
            question_id = str(question.id)
            selected_answer = student_answers.get(f"question_{question.id}")
            print(selected_answer)
            print(question.answer)
            if selected_answer == question.answer:
                obtained_marks += question.marks

            total_marks += question.marks

        percentage_value = (obtained_marks / total_marks) * 100

        result = Result.objects.create(group=Group.objects.get(name='students'), exam=course, marks=obtained_marks, percentage=percentage_value)
        return render(request, 'online_quizz/result.html', {'result': result, 'total_marks': total_marks, 'percentage': percentage_value})

    else:
        course = get_object_or_404(Course, id=course_id)
        questions = course.question_set.all()
        return render(request, 'online_quizz/course_detail.html', {'course': course, 'questions': questions})

def logout_(request):
    logout(request)
    return redirect('online_quizz:home_page')
# @permission_required('online_quizz.view_dashboard',login_url='online_quizz:student_login')
@login_required (login_url='online_quizz:student_login')
def teacher_dashboard(request):

    students = User.objects.filter(groups__name='students')
    courses = Course.objects.all()
    student_count = students.count()
    course_count = Course.objects.count()
    context = {
        'students': students,
        'courses': courses,
        'student_count':student_count,
        'course_count':course_count,
        
    }

    return render(request, 'online_quizz/teacher_dashboard.html', context)
@login_required (login_url='online_quizz:student_login')
def view_profile(request):
    user = request.user
    results = Result.objects.filter(group__name='students')  # Filter results by group name 'students'

    quizzes_count = 0
    overall_percentage = 0.0

    for result in results:
        if result.percentage is not None:
            overall_percentage += result.percentage
            quizzes_count += 1

    overall_percentage = overall_percentage / quizzes_count if quizzes_count > 0 else 0.0

    profile_data = []
    for result in results:
        percentage = result.percentage if result.percentage is not None else 0.0
        total_marks = sum(question.marks for question in result.exam.question_set.all())

        profile_data.append({
            'course_name': result.exam.course_name,
            'marks': result.marks,
            'percentage': percentage,
            'date': result.date,
            'total_marks':total_marks

        })
    
    return render(request, 'online_quizz/profile.html', {'profile_data': profile_data, 'overall_percentage': overall_percentage})
@login_required (login_url='online_quizz:student_login')
def teacher_view(request):
    students = User.objects.filter(groups__name='students')  # Get all users in 'students' group
    student_data = []

    for student in students:
        results = Result.objects.filter(group__name='students', exam__in=Course.objects.all(), group__user=student)
        total_marks = sum(result.marks for result in results)
        overall_percentage = (total_marks / (results.count() * 100)) * 100 if results.count() > 0 else 0

        student_data.append({
            'student': student,
            'results': results,
            'total_marks': total_marks,
            'overall_percentage': overall_percentage,
        })

    return render(request, 'online_quizz/teacher_view.html', {'student_data': student_data})
@permission_required('online_quizz.view_course',login_url='online_quizz:student_login')
def teacher_courses(request):
    courses = Course.objects.all()
    return render(request, 'online_quizz/teacher_courses.html', {'courses': courses})
@permission_required('online_quizz.view_question',login_url='online_quizz:student_login')
def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = course.question_set.all()
    return render(request, 'online_quizz/course_details.html', {'course': course, 'questions': questions})
@permission_required('online_quizz.add_course',login_url='online_quizz:student_login')
def add_course(request):
    if request.method == 'POST':
        # Process form data and save the new course
        course_name = request.POST['course_name']
        description = request.POST['description']
        total_marks = request.POST['total_marks']

        course = Course(course_name=course_name, description=description, total_marks=total_marks)
        course.save()

        return redirect('online_quizz:teacher_courses')

    return render(request, 'online_quizz/add_course.html')
@permission_required('online_quizz.change_course',login_url='online_quizz:student_login')
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        # Update course details
        course.course_name = request.POST['course_name']
        course.description = request.POST['description']
        course.total_marks = request.POST['total_marks']
        course.save()

        return redirect('online_quizz:course_details', course_id=course.id)

    return render(request, 'online_quizz/update_course.html', {'course': course})
@permission_required('online_quizz.delete_course',login_url='online_quizz:student_login')
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        # Delete the course
        course.delete()
        return redirect('online_quizz:teacher_courses')

    return render(request, 'online_quizz/delete_course.html', {'course': course})
@permission_required('online_quizz.add_question',login_url='online_quizz:student_login')
def add_question(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        # Process form data and save the new question
        question = request.POST['question']
        marks = request.POST['marks']
        question_number = request.POST['question_number']
        option1 = request.POST['Option1']
        option2 = request.POST['Option2']
        option3 = request.POST['Option3']
        option4 = request.POST['Option4']
        answer = request.POST['answer']

        question = Question(course=course, question=question, marks=marks,question_number=question_number, option1=option1, option2=option2, option3=option3, option4=option4, answer=answer)
        question.save()

        return redirect('online_quizz:course_details', course_id=course.id)

    return render(request, 'online_quizz/add_question.html', {'course': course})
@permission_required('online_quizz.change_question',login_url='online_quizz:student_login')
def update_question(request, course_id, question_id):
    course = get_object_or_404(Course, id=course_id)
    question = get_object_or_404(Question, id=question_id, course=course)

    if request.method == 'POST':
        # Update question details
        question.question_text = request.POST['question_text']
        question.option1 = request.POST['option1']
        question.option2 = request.POST['option2']
        question.option3 = request.POST['option3']
        question.option4 = request.POST['option4']
        question.answer = request.POST['answer']
        question.save()

        return redirect('course_details', course_id=course.id)

    return render(request, 'online_quizz/update_question.html', {'course': course, 'question': question})
@permission_required('online_quizz.delete_question',login_url='online_quizz:student_login')
def delete_question(request, course_id, question_id):
    course = get_object_or_404(Course, id=course_id)
    question = get_object_or_404(Question, id=question_id, course=course)

    if request.method == 'POST':
        # Delete the question
        question.delete()
        return redirect('online_quizz:course_details', course_id=course.id)

    return render(request, 'online_quizz/delete_question.html', {'course': course, 'question': question})




