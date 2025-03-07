# wiki/models.py
"""
Wiki app models that define the structures for articles and categories.

ArticleCategory has a name, description, and has categories ordered by name.

Article has a title, associated category, and entry (the written content).
Articles have dates for creation and recent updates.
Articles are sorted in descending order based on creation dates.
"""
from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    """
    Data structure for article categories.

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
    Data structure for articles.

    Has a title, associated category, and entry.
    """

    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """Return absolute URL for article page."""
        return reverse('wiki:article_details', args=[self.pk])

    def __str__(self):
        """Return title particularly for display purposes."""
        return self.title

    class Meta:
        """Sort articles by creation date in descending order."""

        ordering = ['-created_on']
