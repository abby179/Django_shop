from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    user table, add below field
    """
    GENDER_CHOICES = (
        ("male", "male"),
        ("female", "female"),
    )
    name = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='female')
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    verify code from mobile. could be saved to redis
    """
    code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=11)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.code
