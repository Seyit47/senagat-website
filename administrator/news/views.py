from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from main.models import *
from .forms import NewsForm


@login_required(login_url='administrator:login')
def news(request):
    news = News.objects.all().order_by('-created_date')

    return render(request, 'administrator/news.html', 
    {'page':'news',
    'news':news})

@login_required(login_url='administrator:login')
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.published_date = timezone.now()
            news.save()
            return redirect('news:news_detail', pk=news.pk)
    else:
        form = NewsForm()
    
    return render(request, 'administrator/news_detail.html', {'form':form,'page':'news'})

def news_edit(request):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.published_date = timezone.now()
            news.save()
            return redirect('news:news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'administrator/news_detail.html', {'form':form,'page':'news'})