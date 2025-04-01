from django.db import models

class studentdetails(models.Model):
    student_email = models.CharField(max_length=50)
    student_name = models.CharField(max_length=50)
    department = models.CharField(max_length=10)
    new_course = models.CharField(max_length=10)


# # Create your models here.
