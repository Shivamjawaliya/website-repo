
from django.db import models

class newcourseenroled(models.Model):
    course_name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=10)
    course_instructor = models.CharField(max_length=30)
    course_complete = models.CharField(max_length=3)
    student_id = models.CharField(max_length=30)
    primary = models.CharField(max_length=50)