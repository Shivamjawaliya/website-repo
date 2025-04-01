from django.db import models


class requestcourse(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    student_email = models.CharField(max_length=20)
    course_teacher = models.CharField(max_length=30)
    primary = models.CharField(max_length=50)
# Create your models here.
class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course_code', 'student_email'], name='unique_course_request')
        ]
