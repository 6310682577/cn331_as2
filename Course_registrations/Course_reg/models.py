from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    subject = models.CharField(max_length=50)
    subject_id = models.CharField(max_length=50)
    credit = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.subject_id} {self.subject} {self.credit}'
    
class Date(models.Model):
    subject_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.CharField(max_length=50)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    seat = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f'{self.subject_id}: {self.section} {self.start_time} {self.end_time} {self.day} {self.seat}'

class Student(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    course_enroll = models.ManyToManyField(Date, related_name='student')

    def __str__(self):
        return f"{self.name.first_name} {self.name.last_name}"