from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Dashboard view
def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, 'core/dashboard.html', context)


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'core/login.html')


# Register view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            messages.error(request, 'Passwords do not match')
            return render(request, 'core/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'core/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'core/register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    
    return render(request, 'core/register.html')


# Forgot Password view
def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if User.objects.filter(email=email).exists():
            messages.success(request, f'Password reset link has been sent to {email}')
        else:
            messages.error(request, 'Email not found in our system')
    
    return render(request, 'core/forgot_password.html')


# Student list view
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})


# Add student view
def add_student(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        Student.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            age=request.POST.get("age"),
            course_id=request.POST.get("course"),
        )
        messages.success(request, 'Student added successfully')
        return redirect('student_list')
    return render(request,'core/add_student.html',{"courses":courses})


# Edit student view
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()

    if request.method == 'POST':
        student.full_name = request.POST.get('full_name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.course_id = request.POST.get('course')
        student.save()
        messages.success(request, 'Student updated successfully')
        return redirect("student_list")

    return render(request, 'core/edit_student.html', {
        "student": student,
        "courses": courses
    })


# Delete student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")


# Course list + add course
def course_list(request):
    if request.method == "POST":
        Course.objects.create(
            name=request.POST.get("name")
        )
        return redirect("course_list")

    courses = Course.objects.all()
    return render(request, "core/course_list.html", {
        "courses": courses
    })


# Delete course
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('login')