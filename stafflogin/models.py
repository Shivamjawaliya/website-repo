from django.db import models

class stafflogin(models.Model):
    staff_email = models.CharField(max_length=50)
    staff_password = models.CharField(max_length=50)
    staff_name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True) 
# # Create your models here.
