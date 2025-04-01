from django.contrib import admin
from stafflogin.models import stafflogin

class servicestafflogin(admin.ModelAdmin):
    list_display=(
        'staff_email',
        'staff_password',
        'staff_name',
        'id'
    )

admin.site.register(stafflogin ,servicestafflogin)

# Register your models here.
