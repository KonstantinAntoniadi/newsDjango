from django.shortcuts import render

def news_home(request):
    data ={
        'title': 'News on page'
    }
    return render(request, 'news/news.html', data)
