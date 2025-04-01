from django.urls import path
from .views import assignment_create, assignment_success
from django.urls import path
from .views import assignment_create, download_pdf
# urls.py
from . import views


urlpatterns = [
    path('', assignment_create, name='assignment_create'),  # Existing assignment create view
    path('download_pdf/<int:assignment_id>/', download_pdf, name='download_pdf'),  # New URL for PDF download
    path('success/', assignment_success, name='assignment_success'),
    path('assignment/<int:assignment_id>/', views.view_assignment, name='view_assignment'),
]
