from django.db import models

# Create your models here.
# Future Plan

# Desiding Role of Teacher
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[('student','student'),('instructor','instructor'),('admin','admin')],
        default='student'
    )
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
