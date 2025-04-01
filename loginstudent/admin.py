from django.contrib import admin
from loginstudent.models import loginstudent

class serviceloginstudentn(admin.ModelAdmin):
    list_display=('username' ,'password' , 'student_name')


admin.site.register(loginstudent,serviceloginstudentn)

# Register your models here.
