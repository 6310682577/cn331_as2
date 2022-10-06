from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.models import User
from Course_reg.models import Course, Student, Date

class CourseViewTest(TestCase):
    def setUp(self):
        User.objects.create(username="It's me", first_name="best", last_name="jun")
        course = Course.objects.create(subject="Thai", subject_id="TH101", credit=3)
        Date.objects.create(subject_id=course, section="100001", start_time="9:30", end_time="12:30",   
                            day="Monday", room="1024", year="2", semester="1", seat=1, status=True)

    def test_course_reg_page(self):
        student = Student.objects.create(name=User.objects.first())

        course = Date.objects.first()
        course.seat = 1
        course.save()

        c = Client()
        c.post(reverse('enroll'), {'student': student.name, 'section': course.section, 'subject_id': course.subject_id.subject_id})

        self.assertEqual(course.seat, second)

        # <input type="hidden" name="student" value="{{ request.user.username }}">
        #                 <input type="hidden" name="section" value="{{ enroll.section }}">
        #                 <button name="subject_id" value="{{ enroll.subject_id.subject_id }}" type="Delete">remove</option>