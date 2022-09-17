from django.urls import path

from Course_reg import views as Cviews
from . import views as Uviews

urlpatterns = [
    path('', Uviews.index, name='index'),
    path('login', Uviews.login_view, name='login'),
    path('logout', Uviews.logout_view, name='logout'),
    path('register', Uviews.register_view, name='register'),
    path('enrolled', Uviews.enrolled_view, name='enrolled'),
    path('enroll', Uviews.enroll, name='enroll'),
    path('del_enroll', Uviews.del_enroll, name='del_enroll'),
    path('../Course_reg', Cviews.course, name='course')
]