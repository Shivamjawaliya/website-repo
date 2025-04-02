
from django.db import models

class grades(models.Model):
    student_id = models.CharField(max_length=30)
    course_name = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    grades = models.CharField(max_length=10)