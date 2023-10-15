from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='student')
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'})
    title_lekcture = models.CharField('описание лекций',max_length=255)
    file1 = models.FileField(upload_to='practices/', blank=True, null=True)
    file2 = models.FileField(upload_to='practices/', blank=True, null=True)
    file3 = models.FileField(upload_to='practices/', blank=True, null=True)
    file4 = models.FileField(upload_to='practices/', blank=True, null=True)
    file5 = models.FileField(upload_to='practices/', blank=True, null=True)
    file6 = models.FileField(upload_to='practices/', blank=True, null=True)
    file7 = models.FileField(upload_to='practices/', blank=True, null=True)
    file8 = models.FileField(upload_to='practices/', blank=True, null=True)
    file9 = models.FileField(upload_to='practices/', blank=True, null=True)
    file10 = models.FileField(upload_to='practices/', blank=True, null=True)
    file11 = models.FileField(upload_to='practices/', blank=True, null=True)
    file12 = models.FileField(upload_to='practices/', blank=True, null=True)
    file13 = models.FileField(upload_to='practices/', blank=True, null=True)
    file14 = models.FileField(upload_to='practices/', blank=True, null=True)
    file15 = models.FileField(upload_to='practices/', blank=True, null=True)
    file16 = models.FileField(upload_to='practices/', blank=True, null=True)
    file17 = models.FileField(upload_to='practices/', blank=True, null=True)
    file18 = models.FileField(upload_to='practices/', blank=True, null=True)
    file19 = models.FileField(upload_to='practices/', blank=True, null=True)
    file20 = models.FileField(upload_to='practices/', blank=True, null=True)
    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User
import uuid 

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    confirmation_code = models.UUIDField(default=uuid.uuid4)