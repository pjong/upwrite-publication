from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article


def dashboard(request):
    sections = ['regional', 'national', 'editorial', 'provincial', 'legal']
    latest_articles = {}

    for section in sections:
        article = Article.objects.filter(section=section, is_published=True).order_by('-created_at').first()
        if article:
            latest_articles[section] = article

    return render(request, 'news/dashboard.html', {'latest_articles': latest_articles})

def section_view(request, section):
    articles_list = Article.objects.filter(section=section, is_published=True).order_by('-created_at')
    paginator = Paginator(articles_list, 3)  # Show 5 per page
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    return render(request, 'news/section.html', {
        'articles': articles,
        'section': section.title()
    })

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'news/article_detail.html', {'article': article})