"""Receives web requests and returns the necessary web response."""
from django.shortcuts import render
from .models import Article, ArticleCategory


def blog_list(request):
    """Return blog_list html file with apt context."""
    categories = ArticleCategory.objects.all().order_by("name")
    articles = Article.objects.all().order_by("-creation_date")

    return render(request, "blog_list.html", {
        "articlecategory": categories,
        "articles": articles
    })


def blog_details(request, id):
    """Return blog_details html file with apt context."""
    article = Article.objects.get(id=id)
    return render(request, "blog_details.html", {"article": article})
