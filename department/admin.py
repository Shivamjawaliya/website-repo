from django.contrib import admin
from department.models import department

class servicedepartment(admin.ModelAdmin):
    list_display=(
    'department_id',
    'department_name',
    )

admin.site.register(department , servicedepartment)
# Register your models here.
