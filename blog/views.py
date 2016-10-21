from django.shortcuts import render, get_object_or_404
from blog.models import Article


# Take the data from the database and render an HTML page from the template


def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article.html', {'article': article})


def test_brython(reqest):
    return render(reqest, 'blog/testbrython.html')
