from django.contrib import admin
from assignment.models import assignment

class Serviceassignment(admin.ModelAdmin):
    list_display=(
    'department_id',
    'course_name',
    'title',
    'decs',
    'status',
    'url',
    )

admin.site.register(assignment , Serviceassignment)

# Register your models here.
