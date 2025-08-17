from django.contrib import admin
from .models import Course, Lecture, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    ordering = ['-created_at']

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_filter = ['course', 'order']
    search_fields = ['title', 'description']
    ordering = ['course', 'order']
    raw_id_fields = ['course']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'enrolled_at']
    list_filter = ['enrolled_at']
    search_fields = ['user__username', 'course__title']
    raw_id_fields = ['user', 'course']
