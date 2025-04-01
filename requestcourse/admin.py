from django.contrib import admin
from requestcourse.models import requestcourse

class servicerequestcourse(admin.ModelAdmin):
    list_display=(
        'id',
    'course_name',
    'course_code',
    'student_email',
    'course_teacher',
    'primary',
    )
admin.site.register(requestcourse , servicerequestcourse)
# Register your models here.
