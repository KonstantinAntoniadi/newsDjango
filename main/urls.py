from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('lessons', views.lessons),
    path('students', views.students)
]