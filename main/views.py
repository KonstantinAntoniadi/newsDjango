from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(requset):
    data = {
        'title': 'Main page',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(requset, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

# def lessons(request):
#     return HttpResponse("<h1>Lessons</h1>")
#
# def students(request):
#     return HttpResponse("<h2><font color=""#fa8e47"">Students</font></h2>")
