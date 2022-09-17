from django.urls import path

from . import views as Cviews
from users import views as Uviews

urlpatterns = [
    path('', Cviews.index, name='Index'),
    path('<int:Course_id>', Cviews.course, name='Course'),
    path('../users', Uviews.index, name='UserIndex')
]
