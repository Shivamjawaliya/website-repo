from django.shortcuts import render, redirect
from .forms import AssignmentForm
from .models import Assignment
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from .models import Assignment
# assignment1/views.py
from django.shortcuts import render, get_object_or_404
from .models import Assignment  # Ensure you have an Assignment model

def view_assignment(request, assignment_id):
    # Retrieve the assignment object or return a 404 if not found
    assignment = get_object_or_404(Assignment, id=assignment_id)
    
    # Render the assignment detail template with the assignment context
    return render(request, 'assignment_detail.html', {'assignment': assignment})

def download_pdf(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    # Return the file response for the PDF stored in the model
    return FileResponse(assignment.pdf_file, content_type='application/pdf')


def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assignment_success')  # Redirect to a success page
    else:
        form = AssignmentForm()
    
    return render(request, 'assignment1/assignment_form.html', {'form': form})

def assignment_success(request):
    return render(request, 'assignment1/success.html')


