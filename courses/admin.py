from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser, Course,Profile

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'user_type', 'date_joined', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        ('Основная информация', {'fields': ('username', 'email', 'password', 'user_type')}),
        ('Права и статус', {'fields': ('is_staff', 'is_active')}),
        ('Временные метки', {'fields': ('date_joined', 'last_login')}),
    )

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'file_count')
    list_filter = ('created_by',)
    search_fields = ('title',)
    readonly_fields = ('created_by',)
    fieldsets = (
        ('Информация о курсе', {'fields': ('title', 'description', 'image', 'created_by', 'title_lekcture')}),
        ('Практические файлы', {'fields': [f'file{i}' for i in range(1, 21)]}),
    )

    def file_count(self, obj):
        return sum(1 for field in [getattr(obj, f'file{i}') for i in range(1, 21)] if field)

    file_count.short_description = 'Количество файлов'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Profile)
