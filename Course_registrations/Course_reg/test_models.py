from django.test import TestCase
from .models import Course, Student, Date
from django.contrib.auth.models import User

# Create your tests here.

class CourseTestCase(TestCase):
    def setUp(self):
        # create Course
        User.objects.create(username="It's me", first_name="best", last_name="jun")
        course = Course.objects.create(subject="Thai", subject_id="TH101", credit=3)
        Date.objects.create(subject_id=course, section="100001", start_time="9:30", end_time="12:30",
                            day="Monday", room="1024", year="2", semester="1", seat=1, status=True)

    def test_seat_avaliable(self):
        course = Date.objects.first()

        self.assertTrue(course.is_seat_avaliable())
    
    def test_seat_not_avaliable(self):
        user1 = User.objects.first()

        student1 = Student.objects.create(name=user1)
        course = Date.objects.first()

        student1.course_enroll.add(course)
        course.seat -= 1

        self.assertFalse(course.is_seat_avaliable())
