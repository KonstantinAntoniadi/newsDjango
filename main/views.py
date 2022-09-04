from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requset):
    return HttpResponse("<h4>Check work</h4>")

def about(request):
    return HttpResponse("<h4>About</h4>")

def lessons(request):
    return HttpResponse("<h1>Lessons</h1>")

def students(request):
    return HttpResponse("<h2><font color=""#fa8e47"">Students</font></h2>")
