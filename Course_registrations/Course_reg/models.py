from django.db import models

# Create your models here.

class Course(models.Model):
    subject = models.CharField(max_length=50)
    subject_id = models.CharField(max_length=50)
    credit = models.IntegerField()
    seat = models.IntegerField()
    users = models.ManyToManyField('auth.User', null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.subject_id} {self.subject} {self.credit} {self.seat}'
    
class Date(models.Model):
    subject_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.CharField(max_length=50)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.subject_id}: {self.section} {self.start_time} {self.end_time} {self.day}'