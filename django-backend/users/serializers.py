from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    enrolled_courses = serializers.SerializerMethodField()

    def get_enrolled_courses(self, obj):
        from courses.serializers import CourseListSerializer
        enrollments = obj.enrollments.select_related('course').all()
        courses = [enrollment.course for enrollment in enrollments]
        return CourseListSerializer(courses, many=True).data
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'role', 'phone', 'password', 'enrolled_courses')
        extra_kwargs = {'password': {'write_only': True}}
