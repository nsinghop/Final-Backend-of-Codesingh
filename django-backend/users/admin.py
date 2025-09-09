from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	model = CustomUser
	list_display = ('username', 'email', 'is_student', 'is_teacher', 'is_staff', 'is_superuser')
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('is_student', 'is_teacher', 'phone')}),
	)
