"""Create models ArticleCategory & Article with appropriate fields."""

from django.db import models
from user_management.models import Profile



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
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        ArticleCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    most_recent_update_date = models.DateTimeField(auto_now=True)
    header_image = models.ImageField(upload_to='article_headers/')

    def __str__(self):
        """Return the name of the Article itself."""
        return self.title

    class Meta:
        """Order the article based on its creation date."""

        ordering = ["-creation_date"]

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    entry = models.TextField()
    most_recent_update_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        """Order the comments based on its creation date."""
        ordering = ["creation_date"]

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
