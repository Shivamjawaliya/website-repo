from django.db import models

class department(models.Model):
    department_id = models.CharField(max_length=10)
    department_name = models.CharField(max_length=30)