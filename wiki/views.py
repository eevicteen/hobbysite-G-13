# wiki/views.py
"""List, detail, create, and update views for Wiki articles."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ArticleCategory, Article, Comment
from .forms import CommentForm, ArticleForm, ArticleUpdateForm, CommentUpdateForm


class ArticleListView(ListView):
    """
    View for the list of article categories.

    Connects corresponding template to the category model.
    """

    model = ArticleCategory
    template_name = 'wiki_list.html'
    context_object_name = 'articlecategory'

    def get_context_data(self, **kwargs):
        """Display categories based on user-made articles or lack thereof."""
        context = super().get_context_data(**kwargs)
        user = self.request.user
        categories = ArticleCategory.objects.all()

        if user.is_authenticated:
            user_articles = Article.objects.filter(author=user.profile)
            all_articles = {
                category: category.articles.exclude(author=user.profile) for category in categories
            }

            context['user_articles'] = user_articles
            context['all_articles'] = all_articles
            context["create_article"] = reverse('wiki:article_create')
        else:
            context['all_articles'] = categories

        return context


class ArticleDetailView(DetailView):
    """
    View for the article(s).

    Connects corresponding template to the article model.
    """

    model = Article
    template_name = 'wiki_details.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        """Provides article contents, comments, and edit option."""
        context = super().get_context_data(**kwargs)
        associated_article = self.get_object()
        more_articles = Article.objects.filter(category=associated_article.category).exclude(id=associated_article.id).order_by("?")[:2]
        comments = Comment.objects.filter(article=associated_article)
        user = self.request.user

        context['more_articles'] = more_articles
        context['article_list_link'] = reverse('wiki:article_list')
        context['comments'] = comments
        if associated_article.header_image:
            context['header_image'] = associated_article.header_image.url
        else:
            context['header_image'] = None
        if user.is_authenticated:
            context['comment_form'] = CommentForm()
            if associated_article.author == user:
                context['edit_article'] = reverse('wiki:article_update', kwargs={'pk': associated_article.pk})
        else:
            context['comment_form'] = None
            context['edit_article'] = None

        return context

    def post(self, request, *args, **kwargs):
        """Handles comment post if user is logged in."""
        associated_article = self.get_object()

        if request.user.is_authenticated and request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user.profile
                comment.article = associated_article
                comment.save()

                return HttpResponseRedirect(reverse('wiki:article_details', kwargs={'pk': associated_article.pk}))
        
        context = self.get_context_data(comment_form=form)
        return self.render_to_response(context)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Handles the creation of new articles by logged-in users."""

    model = Article
    form_class = ArticleForm
    template_name = 'wiki_create.html'

    def form_valid(self, form):
        """Assign logged-in user as the author."""
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to the new article page."""
        return reverse('wiki:article_details', kwargs={'pk': self.object.pk})


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allows updating the contents of articles by logged-in users."""

    model = Article
    form_class = ArticleUpdateForm
    template_name = 'wiki_update.html'

    def test_func(self):
        """Restrict access to just the article's author."""
        article = self.get_object()
        return article.author == self.request.user.profile

    def get_success_url(self):
        """Redirect to article page after updating article."""
        return reverse('wiki:article_details', kwargs={'pk': self.object.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Allows users to update their own comments."""

    model = Comment
    form_class = CommentUpdateForm
    template_name = 'comment_edit.html'

    def test_func(self):
        """Restrict access to just the comment's author."""
        comment = self.get_object()
        return comment.author == self.request.user.profile
    
    def get_success_url(self):
        """Redirect to article page after updating comment."""
        return reverse('wiki:article_details', kwargs={'pk': self.object.article.pk})
