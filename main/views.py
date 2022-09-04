from django.shortcuts import render

# Create your views here.
def index(requset):
    return render(requset, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

# def lessons(request):
#     return HttpResponse("<h1>Lessons</h1>")
#
# def students(request):
#     return HttpResponse("<h2><font color=""#fa8e47"">Students</font></h2>")
