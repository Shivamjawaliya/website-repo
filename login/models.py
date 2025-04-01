from django.db import models

class login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    student_name = models.CharField(max_length=40)

def __str__(self):
        return self.username
# Create your models here.
