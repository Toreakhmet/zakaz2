from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.exceptions import PermissionDenied
import os
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm
import chardet
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponse
def home(request):
    context=Course.objects.all()
    return render(request,'home.html',{'course':context})




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)  # Создаем профиль для пользователя

            # Отправляем письмо для подтверждения
            send_mail(
                'Подтвердите ваш аккаунт',
                f'Подтвердите ваш аккаунт, перейдя по следующей ссылке: '
                f'http://pokerman228{reverse("confirm_email", args=[profile.confirmation_code])}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
    
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    return render(request,'profile.html')





def is_teacher(user):
    return user.is_authenticated and getattr(user, 'user_type', None) == 'teacher'

@user_passes_test(is_teacher)
@login_required  
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user  
            course.save()
            return redirect('home')
    else:
        form = CourseForm(initial={'created_by': request.user}) 

    return render(request, 'create_course.html', {'form': form})
def view_file(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return render(request, '404.html')

    file_path = course.file1.path

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            bytes_content = f.read()

            # Определение кодировки файла
            result = chardet.detect(bytes_content)
            charenc = result['encoding']

            try:
                content = bytes_content.decode(charenc)
            except UnicodeDecodeError:
                content = "Cannot decode file"
    else:
        content = "File not found."

    return render(request, 'view_file.html', {'content': content})
def course_detail(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        file_path = course.file1.path
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "File not found."
    except Course.DoesNotExist:
        return render(request, '404.html')

    return render(request, 'course_detail.html', {'course': course, 'content': content})
# views.py

def confirm_email(request, confirmation_code):
    try:
        profile = Profile.objects.get(confirmation_code=confirmation_code)
    except Profile.DoesNotExist:
        return HttpResponse('Неверный код подтверждения')
    
    profile.email_confirmed = True
    profile.save()
    return HttpResponse('Аккаунт подтвержден')
