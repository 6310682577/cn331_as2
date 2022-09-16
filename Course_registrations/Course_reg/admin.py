from django.contrib import admin

from .models import Course, Date, Student

# Register your models here.

admin.site.register(Course)
admin.site.register(Date)
admin.site.register(Student)