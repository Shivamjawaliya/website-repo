from django.contrib import admin
from login.models import login


class servicelogin(admin.ModelAdmin):
    list_display=('username' ,'password' , 'student_name')


admin.site.register(login,servicelogin)

# Register your models here.
