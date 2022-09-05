from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    # path('lessons', views.lessons),
    # path('students', views.students)
]