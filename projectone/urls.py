"""
URL configuration for projectone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projectone import views
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home ),
    path('course', views.course ),
    path('contact', views.contact ),
    path('bothlogin', views.bothlogin ),
    path('studentlogin_page', views.studentlogin_page ),
    path('stafflogin_page', views.stafflogin_page ),
    path('student_register', views.student_register ),
    path('studentprofile', views.studentprofile ),
    path('staffhome', views.staffhome ),
    path('tech', views.tech ),
    path('sendrequest' , views.sendrequest , name="sendrequest"),
    path('requestsubmite' , views.requestsubmite , name="requestsubmite"),
    path('handle_course_request' , views.handle_course_request , name="handle_course_request"),
    path('submitedsucessful' , views.requestsubmite),
    path('uplode' , views.uplode),
    


]
