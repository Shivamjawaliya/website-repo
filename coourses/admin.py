from django.contrib import admin
from coourses.models import coourses

class Servicecoourses(admin.ModelAdmin):
    list_display=(
    'department_id',
    'course_name',
    'course_code',
    'course_instructor',
    'course_complete'
    )

admin.site.register(coourses , Servicecoourses)

# Register your models here.
