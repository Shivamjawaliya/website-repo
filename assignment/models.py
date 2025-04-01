from django.db import models

class assignment(models.Model):
    department_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    decs = models.CharField(max_length=1000)
    status = models.CharField(max_length=30)
    url = models.CharField(max_length=10000)
