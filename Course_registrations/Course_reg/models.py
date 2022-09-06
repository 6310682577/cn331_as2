from django.db import models

# Create your models here.

class Course(models.Model):
    subject = models.CharField(max_length=50)
    subject_id = models.CharField(max_length=50)
    credit = models.IntegerField()
    seat = models.IntegerField()

    def __str__(self):
        return f'{self.id}: {self.subject_id} {self.subject} {self.credit} {self.seat}'
    
class Date(models.Model):
    section = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.CharField(max_length=50)
    day = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.time} {self.day}'
    