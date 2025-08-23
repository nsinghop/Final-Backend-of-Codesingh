from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LectureViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lectures', LectureViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
