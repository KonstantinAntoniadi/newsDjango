from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
@login_required
def news_home(request):
    news = Articles.objects.order_by('-date')
    count_visits = request.session.get('count_visits', 0)
    request.session['count_visits'] = count_visits + 1
    data = {
        'title': 'News on page',
        'news': news,
        'count_visits': count_visits
    }

    return render(request, 'news/news.html', data)

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'
@login_required
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