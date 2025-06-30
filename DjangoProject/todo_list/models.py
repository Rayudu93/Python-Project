from django.db import models
from django.contrib.auth.models import User  # 👈 import the built-in User model

class Task(models.Model):
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task
