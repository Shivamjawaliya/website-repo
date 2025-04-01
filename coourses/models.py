from django.db import models

class coourses(models.Model):
    department_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=10)
    course_instructor = models.CharField(max_length=30)
    course_complete = models.CharField(max_length=3)
# Create your models here.