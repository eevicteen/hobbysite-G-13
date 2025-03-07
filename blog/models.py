"""Create models ArticleCategory & Article with appropriate fields."""

from django.db import models


class ArticleCategory(models.Model):
    """Create ArticleCategory with appropriate field, sorted alphabetically."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """Return the name of the Article Category."""
        return self.name

    class Meta:
        """Order the article categorys alphabetically."""

        ordering = ["name"]


class Article(models.Model):
    """Create Article model with appropriate field, sorted by date."""

    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    most_recent_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the name of the Article itself."""
        return self.title

    class Meta:
        """Order the article based on its creation date."""

        ordering = ["-creation_date"]
