# education_portal/urls.py

from django.contrib import admin
from django.urls import path, include
from courses import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('',include('django.contrib.auth.urls')),
    path('register',views.register,name='register')
    #path('accounts/', include('allauth.urls')),
    #path('courses/', include('courses.urls')),
]
