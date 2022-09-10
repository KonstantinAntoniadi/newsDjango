from django.shortcuts import render
from .models import Articles
def news_home(request):
    news = Articles.objects.all()
    data = {
        'title': 'News on page',
        'news': news
    }
    return render(request, 'news/news.html', data)
