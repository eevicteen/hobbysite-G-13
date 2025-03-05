from django.shortcuts import render, get_object_or_404

from .models import Article, ArticleCategory

def blog_list(request):
    categories = ArticleCategory.objects.all().order_by("name") 
    articles = Article.objects.all().order_by("-creation_date")

    return render(request, "blog_list.html", {
        "articlecategory": categories,  
        "articles": articles  
    })

def blog_details(request, id):
    article = Article.objects.get(id=id)
    return render(request, "blog_details.html", {"article": article})