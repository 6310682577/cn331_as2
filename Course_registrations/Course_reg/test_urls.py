from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.models import User
from .models import Course, Student, Date

class CourseUrlTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="It's me", first_name="best", last_name="jun")
        course = Course.objects.create(subject="Thai", subject_id="TH101", credit=3)
        Date.objects.create(subject_id=course, section="100001", start_time="9:30", end_time="12:30",
                            day="Monday", room="1024", year="2", semester="1", seat=1, status=True)

        Student.objects.create(name=User.objects.first())

    def test_index_view_status_code(self):
        c = Client()
        response = c.get(reverse('Index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        c = Client()
        response = c.get(reverse('Index'))
        self.assertEqual(response.context['Courses'].count(), 1)

    def test_valid_course_page(self):
        c = Client()
        course = Course.objects.first()
        response = c.get(reverse('Course', args=(course.id,)))
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_page(self):
        max_id = Course.objects.all().aggregate(Max("id"))['id__max']

        c = Client()
        response = c.get(f'Course/{max_id+1}')
        self.assertEqual(response.status_code, 404)
