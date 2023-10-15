# education_portal/urls.py
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from courses import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('auth/',include('django.contrib.auth.urls')),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('create_course',views.create_course,name='create_course'),
    path('view/<int:course_id>/', views.view_file, name='view_file'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('confirm_email/<uuid:confirmation_code>/', views.confirm_email, name='confirm_email'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)