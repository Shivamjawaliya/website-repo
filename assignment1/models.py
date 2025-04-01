from django.db import models

class Assignment(models.Model):
    department_id = models.CharField(max_length=50)  # Foreign key later if needed
    course_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField()  # Use TextField for descriptions
    status = models.BooleanField(default=True)  # Active/Inactive
    file_pdf = models.FileField(upload_to='uploads/pdfs/')  # File upload field

    def __str__(self):
        return self.title
