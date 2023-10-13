# courses/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request,'home.html')


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
