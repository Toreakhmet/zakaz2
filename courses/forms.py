from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title', 'description', 'image',
            'file1', 'file2', 'file3', 'file4',
            'file5', 'file6', 'file7', 'file8', 'file9', 'file10',
            'file11', 'file12', 'file13', 'file14', 'file15', 'file16',
            'file17', 'file18', 'file19', 'file20'
        ]
