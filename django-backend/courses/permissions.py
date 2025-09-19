from rest_framework.permissions import BasePermission
from courses.models import Enrollment

class IsEnrolledOrInstructor(BasePermission):
    """
    Allows access only to enrolled users or instructors of the course.
    """
    def has_object_permission(self, request, view, obj):
        course = getattr(obj, 'course', obj)
        if request.user.is_staff:
            return True
        if hasattr(course, 'instructors') and course.instructors.filter(pk=request.user.pk).exists():
            return True
        return Enrollment.objects.filter(user=request.user, course=course, active=True).exists()

class IsInstructor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'instructor' or request.user.is_staff

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' or request.user.is_staff

class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        course = getattr(obj, 'course', obj)
        return Enrollment.objects.filter(user=request.user, course=course, active=True).exists()
