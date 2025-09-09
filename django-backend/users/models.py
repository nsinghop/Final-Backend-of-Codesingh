from django.db import models

# Create your models here.
# Future Plan

# Desiding Role of Teacher
# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # extra fields
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
