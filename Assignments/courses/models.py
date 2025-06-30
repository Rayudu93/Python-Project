# courses/models.py
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)  # e.g., '6 weeks', '3 months'

    def __str__(self):
        return self.title
