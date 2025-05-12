"""Receives web requests and returns the necessary web response."""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, ArticleCategory
from user_management.models import Profile
from .forms import ArticleForm, ArticleCategoryForm, CommentForm, ArticleImageForm


@login_required
def blog_list(request):
    """Return blog list with user-specific and categorized articles."""
    user_profile = request.user.profile  # get the Profile associated with the logged-in User

    categories = ArticleCategory.objects.all()

    # User's own articles
    user_articles = Article.objects.filter(author=user_profile)

    # All articles grouped by category
    categorized_articles = {}
    for category in categories:
        categorized_articles[category] = Article.objects.filter(
            category=category)

    return render(request, "blog_list.html", {
        "user_articles": user_articles,
        "categorized_articles": categorized_articles
    })


@login_required
def blog_details(request, id):
    """Return blog_details html file with apt context."""
    article = Article.objects.get(id=id)
    return render(request, "blog_details.html", {"article": article})


@login_required
def add_article(request):
    """Allows logged-in users to create a new article."""
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            article.author = profile
            article.save()
            return redirect("blog:blog_list")
    return render(request, "add_article.html", {"form": form})
