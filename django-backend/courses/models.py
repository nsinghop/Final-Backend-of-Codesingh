from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    instructors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='courses_teaching')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    thumbnail = models.URLField(blank=True, help_text="Course thumbnail image URL")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    course = models.ForeignKey(Course, related_name="lectures", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=200, blank=True, help_text="Topic of the lecture")
    lecture_type = models.CharField(max_length=10, choices=[('Live', 'Live'), ('Recorded', 'Recorded')], default='Recorded', help_text="Type of lecture: Live or Recorded")
    upload_date = models.DateTimeField(null=True, blank=True, help_text="Lecture uploading date")
    youtube_url = models.URLField(help_text="YouTube video URL")
    questions = models.JSONField(default=list, help_text="List of external question links (LeetCode, GeeksforGeeks, etc.)")
    code = models.TextField(blank=True, null=True, help_text="Python code snippet")
    description = models.TextField(help_text="Lecture description")
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    purchased = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
# Add stubs for additional models
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

class Badge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    awarded_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
