from django.contrib import admin
from assignmentsubmited.models import assignmentsubmited

class Serviceassignmentsubmited(admin.ModelAdmin):
    list_display=(
    'course_name',
    'username',
    'title',
    'pdf_file',
    )

admin.site.register(assignmentsubmited, Serviceassignmentsubmited)


# Register your models here.
