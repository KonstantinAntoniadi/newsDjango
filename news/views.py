from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
def news_home(request):
    news = Articles.objects.order_by('-date')
    data = {
        'title': 'News on page',
        'news': news
    }
    return render(request, 'news/news.html', data)

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save();
            return redirect('news_home ')
        else:
            error = 'Form is incorrect'

    form = ArticlesForm()
    data = {
        'title': 'Form for add news',
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)