from django.contrib import admin
from studentdetails.models import studentdetails

class servicestudentdetails(admin.ModelAdmin):
    list_display=(
    'student_email',
    'student_name',
    'department',
    'new_course',
    )

admin.site.register(studentdetails ,servicestudentdetails)

# Register your models here.
