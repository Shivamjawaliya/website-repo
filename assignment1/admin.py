from django.contrib import admin
from .models import Assignment
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'course_name', 'title']
admin.site.register(Assignment , AssignmentAdmin)
