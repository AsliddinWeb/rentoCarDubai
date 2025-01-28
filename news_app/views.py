from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import News, Category

def news_page(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 9)

    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    ctx = {
        'news': news,
    }

    return render(request, 'news.html', ctx)

def news_category_page(request, pk):
    category = get_object_or_404(Category, pk=pk)

    news_list = News.objects.filter(category=category)
    paginator = Paginator(news_list, 9)

    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    ctx = {
        'news': news,
    }

    return render(request, 'news.html', ctx)

def news_detail_page(request, pk):
    new = get_object_or_404(News, pk=pk)

    ctx = {
        'new': new
    }

    return render(request, 'news-detail.html', ctx)
