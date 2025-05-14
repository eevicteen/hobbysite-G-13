"""Receives web requests and returns the necessary web response."""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, ArticleCategory
from user_management.models import Profile
from .forms import ArticleForm, ArticleCategoryForm, CommentForm, ArticleImageForm, ArticleUpdateForm


@login_required
def blog_list(request):
    """Return blog list with user-specific and categorized articles."""
    user_profile = request.user.profile
    categories = ArticleCategory.objects.all()
    user_articles = Article.objects.filter(author=user_profile)
    categorized_articles = {}
    for category in categories:
        categorized_articles[category] = Article.objects.filter(
            category=category)
    return render(request, "blog_list.html", {
        "user_articles": user_articles,
        "categorized_articles": categorized_articles
    })


def blog_details(request, id):
    """Return blog_details html file with apt context."""
    article = Article.objects.get(id=id)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            profile = Profile.objects.get(user=request.user)
            comment.author = profile
            comment.save()
            print(comment.entry)
            return redirect('blog:blog_detail', article.id)
    comments = article.comment_set.all().order_by('-creation_date')
    other_articles = Article.objects.filter(
        author=article.author).exclude(pk=article.pk)[:2]
    return render(request, 'blog_details.html', {
        'article': article,
        'comment_form': form,
        'comments': comments,
        'other_articles': other_articles,
    })

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

@login_required
def article_update(request, id):
    """Allows logged-in users to update their article."""
    article = get_object_or_404(Article, pk=id)
    if str(article.author) != str(request.user):
        # print (request.user)
        # print (article.author)
        # redirects unauthorized users back to blog_list.
        return redirect("blog:blog_list")
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            instance = form.save()
            return redirect('blog:blog_detail', article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'add_article.html', {'form': form, 'article': article})
