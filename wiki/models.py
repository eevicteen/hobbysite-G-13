# wiki/models.py
"""
Wiki app models for articles, categories, and comments.

ArticleCategory has a name, description, and has categories ordered by name.

Article has a title, associated category, and entry (the written content).
Articles have dates for creation and recent updates.
Articles are sorted in descending order based on creation dates.

Comment has an entry, author, and dates for creation and most recent update.
Comments are sorted in ascending order based on creation dates.
"""
from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ArticleCategory(models.Model):
    """
    Article category model.

    Has a name and description.
    """

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """Return category name particularly for display purposes."""
        return self.name

    class Meta:
        """Sort categories by name (ascending, alphabetical)."""

        ordering = ['name']


class Article(models.Model):
    """
    Article model.

    Has a title, author, associated category, entry, and header.
    """

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        related_name="wiki_articles"
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles"
    )
    entry = models.TextField()
    header_image = models.ImageField(upload_to="article_headers", null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """Return absolute URL for article page."""
        return reverse('wiki:article_details', args=[self.pk])

    def __str__(self):
        """Return the article's title."""
        return self.title

    class Meta:
        """Sort articles by creation date in descending order."""

        ordering = ['-created_on']

class Comment(models.Model):
    """
    Comment model.

    Has an entry and associated author & article.
    """

    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name="wiki_comments"
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Sort comments by creation date in ascending order."""

        ordering = ['created_on']
