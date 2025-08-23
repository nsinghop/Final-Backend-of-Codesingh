from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Course, Lecture
from .serializers import CourseSerializer, CourseListSerializer, LectureSerializer

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseSerializer
    
    @action(detail=True, methods=['get'])
    def lectures(self, request, pk=None):
        """Get all lectures for a specific course"""
        try:
            course = self.get_object()
            lectures = course.lectures.all()
            serializer = LectureSerializer(lectures, many=True)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(
                {'error': 'Course not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )

class LectureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [AllowAny]
