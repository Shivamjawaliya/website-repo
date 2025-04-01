from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render,redirect
from stafflogin.models import stafflogin as staffloginmodel
from login.models import login as loginmodel
from studentdetails.models import studentdetails as studentdetailsmodel
from department.models import department as DepartmentModel
from coourses.models import coourses as cooursesmodel
from requestcourse.models import requestcourse as requestcoursemodel
from newcourseenroled.models import newcourseenroled as new_course_enrolled
from assignment.models import assignment as assignmentmodel
from assignment1.models import Assignment as assignment1model
from django.shortcuts import render, redirect


def home(request):
    return render(request , 'home.html')

def course(request):
    return render(request , 'course.html')

def contact(request):
    return render(request , 'contact.html')

def bothlogin(request):
    return render(request , 'bothlogin.html')

def studentlogin_page(request):
    output=""
    if request.method == "POST":
        student_email = request.POST.get('studentemail')
        student_password = request.POST.get('studentpassword')
        check = loginmodel.objects.filter(username = student_email).first()
        if check :
            if check.password == student_password:
                student_details = studentdetailsmodel.objects.filter(student_email =student_email).first()
                student_department = DepartmentModel.objects.filter(department_id = student_details.department).first()
                studen_course = cooursesmodel.objects.filter(department_id =student_details.department)
                other_course = cooursesmodel.objects.exclude(department_id =student_details.department)
                new_course = new_course_enrolled.objects.filter(student_id = student_email)
                new_cr = other_course
                assignmnet = assignment1model.objects.filter(department_id=student_details.department)
                new_assign = new_course_enrolled.objects.filter(student_id = student_email)
                new_course_assignments = []

# Loop over each course the student is enrolled in
                for n in new_assign:
                    # Retrieve the assignments for each course and add them to the all_assignments list
                    course_assignments = assignment1model.objects.filter(course_name = n.course_name)
                    new_course_assignments.extend(course_assignments)  # Add the retrieved assignments to the list

                # Now, all_assignments will contain all assignments related to the student's courses
                # You can pass this to the context when rendering the template
                
                
                # print(type(new_assignment))
                # for n in new_assign:
                #     print(assignmentmodel.objects.filter(course_name = n.course_name))
                # print(new_assignment)
                
                if new_course.count() != 0:
                    for n in new_course:
                        new3 =cooursesmodel.objects.exclude(department_id =student_details.department)
                # for n in other_course:
                #     print(n.course_code)
                    for n in new_course:
                        new4 = n.course_code
                # for n in new3:
                #     print(n.course_code)
                    new5 = other_course.exclude(course_code = n.course_code)
                if new_course.count() == 0:
                    new5 = other_course
                
                output ="login sucessful"
                return render(request , 'studentprofile.html' , {'student_details' :student_details ,
                'student_department' : student_department.department_name ,
                'courses' :studen_course,
                'other_course' : new5,
                'new_course' : new_course ,
                'assignmnet' : assignmnet ,
                'new_course_assignments' : new_course_assignments})
            else:
                output = "incorrect passsword"
        else:
            output = "user not found"


    return render(request , 'studentlogin_page.html' , {'output' :output})

def stafflogin_page(request):
    output =""
    if request.method == "POST":
        staff_email = request.POST.get('staffemail')
        staff_password = request.POST.get('staffpassword')
        check = staffloginmodel.objects.filter(staff_email = staff_email).first()
        requests = requestcoursemodel.objects.filter(course_teacher = check.staff_name)
        course = cooursesmodel.objects.filter(course_instructor=check.staff_name).first()
        
        # print(staff_email)
        # print(staff_password)
        # print(check)

        if check:
            if check.staff_password != staff_password:
                output = "invalid password"
            elif check.staff_password == staff_password:
                output = "Login sucessful"
                return render(request , 'staffhome.html' , {'staff' : check , 'requests' :requests , 'course' : course.course_name , 'department' : course.department_id})
        else:
            output = "user not found"
    return render(request , 'stafflogin_page.html' , {'output' : output })

def student_register(request):
    if request.method =="POST":
        studentname = request.POST.get('studentname')
        studentemail = request.POST.get('studentemail')
        studentpassword = request.POST.get('studentpassword')
        en = studentdetailsmodel(student_email = studentemail , student_name = studentname)
        en.save()
        en2 = loginmodel(username=studentemail , password = studentpassword ,student_name= studentname)
        en2.save()

    return render(request , 'student_register.html')

def studentprofile(request):
    return render(request , 'studentprofile.html')

def staffhome(request):
    return render(request , 'staffhome.html')

def tech(request):
    newstudent = studentdetailsmodel.objects.filter(department="")[:1]
    Depart = DepartmentModel.objects.all()

    if request.method == "POST":
        student_username = newstudent[0].student_email
        student_dep = request.POST.get('student_department')

        
        
        studentdetailsmodel.objects.filter(student_email = student_username).update(
        department=student_dep
        )
        # print(student_Id)  
    return render(request , 'tech.html' ,{ 'newstudent' : newstudent,
    'department' : Depart})


def sendrequest(request):
    if request.method == "POST":
        new_course = request.POST.get('new_course_name')
        username = request.POST.get('new_course')
        newcourse = cooursesmodel.objects.filter(course_code = new_course )

    return render(request , 'sendrequest.html' , {'requestcourse' : new_course
    , 'newcourse' :newcourse.first() ,
    'username' : username})

def requestsubmite(request):
    output =""
    if request.method == "POST":
        course_code = request.POST.get('course_code')
        student_username = request.POST.get('student_username')
        course_name = request.POST.get('course_name')
        primary = student_username+course_name
        course_techer = cooursesmodel.objects.filter(course_name = course_name ).first().course_instructor
        output = "your request is submited"
        check = requestcoursemodel.objects.filter(primary = primary)
        if check.count() != 0:
            send = "you are already send the regestation request"
            print(check.count())
            return render(request , "submitedsucessful.html" ,{'output' :send })
        en = requestcoursemodel(student_email = student_username,course_code = course_code,course_name = course_name ,
        course_teacher=course_techer , primary = primary )
        en.save()
        
    send = "your request is send to the subject cordinator"
    return render(request , "submitedsucessful.html" ,{ 'output' : send})

def handle_course_request(request):
    if request.method == "POST":
        student_id = request.POST.get('student__Id')
        course__Id = request.POST.get('course__Id')
        action = request.POST.get('action')
        primar = student_id +course__Id
        course =cooursesmodel.objects.filter(course_name = course__Id).first()
        request_H = requestcoursemodel.objects.filter(student_email=student_id,course_name= course__Id).first().delete()
        if action=="confirm":
            en = new_course_enrolled( student_id=student_id , course_name = course.course_name , course_code = course.course_code , course_instructor =course.course_instructor , course_complete = course.course_complete , primary = primar)
            en.save()
        # print(action)
        # print(student_id) # Redirect to the appropriate page after processing
        # print(course__Id) # Redirect to the appropriate page after processing
        # print(action) # Redirect to the appropriate page after processing
    # If the request method is not POST, render the page normally # Adjust this to get the list of courses
    return render(request, 'handle_course_request.html')

# def uplode(request):
#     if request.method == 'POST':
#         titel = request.POST.get('title')
#         desc = request.POST.get('desc')
#         status = request.POST.get('status')
#         print("hello")
#         print(titel , desc, status)
#     return render(request, 'uplode.html')



def uplode(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        status = request.POST.get('status') == 'on'  # Convert checkbox to boolean
        department_id = request.POST.get('department_id')  # Assuming you have this field in your form
        course_name = request.POST.get('course_name')  # Assuming you have this field in your form
        file_pdf = request.FILES.get('file_pdf')  # Get the uploaded file

        # Create a new Assignment instance and save it to the database
        assignment = assignment1model(
            title=title,
            desc=desc,
            status=status,
            department_id=department_id,
            course_name=course_name,
            file_pdf=file_pdf
        )
        assignment.save()  # Save the instance to the database

        return HttpResponse("submited")  # Redirect to a success page after saving

    return render(request, 'uplode.html')

