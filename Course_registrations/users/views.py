from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


from Course_reg.models import Course, Date

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
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
    return render(request, 'users\login.html', {
        'message': 'You are Logged out'
    })

def register_view(request):
    if request.method == "POST":
        searched = str(request.POST['searched']).upper()
        if searched == 'SM':
            date = Date.objects.filter(subject_id__subject_id__contains=searched).order_by('subject_id')
        else:
            date = Date.objects.filter(subject_id__subject_id__contains=searched).exclude(subject_id__subject_id__contains='SM').order_by('subject_id')
        return render(request, 'users/register.html',{
            'searched' : searched,
            'Dates' : date
        })
    else:
        date = Date.objects.exclude(subject_id__subject_id__contains='SM')
        return render(request, 'users/register.html', {
            'Dates' : date
        })

def enroll(request, course_id):
    if request.method == "POST":
        course = Course.objects.get(pk=course_id)
