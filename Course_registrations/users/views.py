from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from Course_reg.models import Course, Date, Student

# Create your views here.

def index(request):
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse('admin:index'))
    elif not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'users/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credential.'
            })
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'You are Logged out'
    })

def register_view(request):
    enroll = Student.objects.get(name__username=request.user).course_enroll
    if request.method == "POST":
        searched = str(request.POST['searched']).upper()
        date = Date.objects.filter(subject_id__subject_id__contains=searched)
        if searched == 'SM':
            date = date.order_by('subject_id')
        # elif enroll.get(subject_id=date.subject_id) != None:
        #     date = date.exclude(subject_id__in=enroll.all().values_list('subject_id'))
        # elif enroll.course_enroll.get(subject_id=date.section) != None:
        #     date = date.exclude(section__in=enroll.all().values_list('section'))
        else:
            date = date.exclude(subject_id__subject_id__contains='SM').order_by('subject_id')
    else:
        searched = None
        date = Date.objects.exclude(subject_id__subject_id__contains='SM')

    # enroll = Student.objects.get(name__username=request.user).course_enroll

    return render(request, 'users/register.html',{
        'searched' : searched,
        'Dates' : date,
        'Enroll' : enroll
    })

def enroll(request):
    if request.method == "POST":
        date = Date.objects.get(subject_id__subject_id=request.POST['subject_id'], section=request.POST['section'])
        student = Student.objects.get(name__username=request.user)
        if date not in student.course_enroll.all():
            Date.objects.filter(subject_id__subject_id=request.POST['subject_id'], section=request.POST['section']).update(seat=(date.seat - 1))
            if date.seat == 0:
                pass
        student.course_enroll.add(date)
        return HttpResponseRedirect(reverse('register'))

def del_enroll(request):
    if request.method == "POST":
        date = Date.objects.get(subject_id__subject_id=request.POST['subject_id'], section=request.POST['section'])
        student = Student.objects.get(name__username=request.user)
        if date in student.course_enroll.all():
            Date.objects.filter(subject_id__subject_id=request.POST['subject_id'], section=request.POST['section']).update(seat=(date.seat + 1))
        student.course_enroll.remove(date)
        return HttpResponseRedirect(reverse('register'))
