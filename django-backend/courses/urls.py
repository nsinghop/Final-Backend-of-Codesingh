from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LectureViewSet, EnrollmentViewSet, AssignmentViewSet, SubmissionViewSet, QuizViewSet, QuestionViewSet, ChoiceViewSet, NotificationViewSet, BadgeViewSet, ChatMessageViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lectures', LectureViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'badges', BadgeViewSet)
router.register(r'chat-messages', ChatMessageViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
