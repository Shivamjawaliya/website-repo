from django.db import models

class loginstudent(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    student_name = models.CharField(max_length=40)
# Create your models here.
