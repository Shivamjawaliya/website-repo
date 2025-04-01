from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['department_id', 'course_name', 'title', 'desc', 'status', 'file_pdf']

    file_pdf = forms.FileField(required=True)
