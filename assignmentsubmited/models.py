from django.db import models

class assignmentsubmited(models.Model):
    course_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='assignments/')  # Directory where files will be stored
    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the assignment was submitted

    def __str__(self):
        return f"{self.title} by {self.username}"
