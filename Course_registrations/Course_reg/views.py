from django.shortcuts import render

from .models import Course
# Create your views here.

def index(request):
    course = Course.objects.exclude(subject_id__contains="SM").all()
    return render(request, 'Courses/index.html', {
        'Courses': course
    })

def course(request, Course_id):
    course = Course.objects.get(id=Course_id)
    return render(request, 'Courses/course.html', {
        'Courses': course
    })