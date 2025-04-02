from django.contrib import admin
from grades.models import grades

class Servicegrades(admin.ModelAdmin):
    list_display=(
    'student_id',
    'course_name',
    'title',
    'grades'
    )

admin.site.register(grades , Servicegrades)
# Register your models here.



