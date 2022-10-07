from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.models import User
from Course_reg.models import Course, Student, Date

class CourseViewTest(TestCase):
    def setUp(self):
        User.objects.create(username="It's me", first_name="best", last_name="jun", password="Me123")
        course = Course.objects.create(subject="Thai", subject_id="TH101", credit=3)
        Date.objects.create(subject_id=course, section="100001", start_time="9:30", end_time="12:30",   
                            day="Monday", room="1024", year="2", semester="1", seat=1, status=True)

    # test enroll method
    def test_enroll(self):
        student = Student.objects.first()

        course = Date.objects.first()
        course.seat = 1

        c = Client()
        c.post(reverse('enroll'), {'student': student.name, 'section': course.section, 'subject_id': course.subject_id.subject_id})
        
        self.assertEqual(Date.objects.get(subject_id=course.subject_id, section=course.section).seat, 0)
    

    # test del enroll method
    def test_del_enroll(self):
        student = Student.objects.first()

        course = Date.objects.first()
        course.seat = 0

        c = Client()
        c.post(reverse('del_enroll'), {'student': student.name, 'section': course.section, 'subject_id': course.subject_id.subject_id})
        
        self.assertEqual(Date.objects.get(subject_id=course.subject_id, section=course.section).seat, 1)

    # test enrolled view context
    def test_enrolled_view_context(self):
        student = Student.objects.first()
        student.course_enroll.add(Date.objects.first())
        self.client.force_login(student.name)
        response = self.client.post(reverse('enrolled'), {'student': student.name})
        self.assertEqual(response.context['Enrolled'].count(), 1)

    def test_search(self):
        student = Student.objects.first()
        self.client.force_login(student.name)
        searched = self.client.post(reverse('register'), {'student': student.name, 'searched': 'TH'}).context['searched']
        self.assertEqual(searched, 'TH')
        searched = self.client.post(reverse('register'), {'student': student.name, 'searched': 'SM'}).context['searched']
        self.assertEqual(searched, 'SM')

class TestUser(TestCase):
    def setUp(self):
        User.objects.create(username="It's me", first_name="best", last_name="jun", password="Me123")

    def test_index(self):
        self.client = Client()
        self.client.login(username='It\'s me', password='Me123')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        self.client = Client()
        response = self.client.post(reverse('login'), {'username': 'It\'s me', 'password': 'Me123'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client = Client()
        self.client.login(username='It\'s me', password='Me123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
