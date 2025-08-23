from rest_framework import serializers
from .models import Course, Lecture

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
<<<<<<< HEAD
        fields = ['id', 'title', 'youtube_url', 'questions', 'code', 'description', 'order']
=======
        fields = [
            'id', 'title', 'topic', 'lecture_type', 'upload_date',
            'youtube_url', 'questions', 'code', 'description', 'order'
        ]
>>>>>>> bd6ddda (Complier added)

class CourseSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'thumbnail', 'created_at', 'lectures']

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'thumbnail', 'created_at']
