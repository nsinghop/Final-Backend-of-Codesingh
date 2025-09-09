from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField(max_length=170)

    thumbnail = models.URLField(blank=True, help_text="Course thumbnail image URL")
    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name="courses"
    # )


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="enrollments", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Prevent duplicate enrollments

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
