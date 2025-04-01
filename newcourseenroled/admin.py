from django.contrib import admin
from newcourseenroled.models import newcourseenroled

class Servicenewcourseenroled(admin.ModelAdmin):
    list_display=(
    'id',
    'course_name',
    'course_code',
    'course_instructor',
    'course_complete',
    'student_id',
    'primary'
    )

admin.site.register(newcourseenroled , Servicenewcourseenroled)
# Register your models here.



