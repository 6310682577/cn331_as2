from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Course_id>', views.course, name='Course'),
]
