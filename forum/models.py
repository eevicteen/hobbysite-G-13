"""Create models PostCategory & Post with appropriate fields."""

from django.db import models
from django.urls import reverse


class PostCategory(models.Model):
    """Create PostCategory with appropriate field, sorted alphabetically."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """Return the name of the Post Category."""
        return self.name

    class Meta:
        "Order the post categories alphabetically."
        ordering = ["name"]


class Post(models.Model):
    """Create Post model with appropriate field, sorted by date."""

    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PostCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    most_recent_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the name of the Post itself."""

        return self.title

    def get_absolute_url(self):
        """Return the url of the Post itself."""

        return reverse('forum:detail', args=[self.pk])

    class Meta:
        """Order the post based on its creation date."""
        ordering = ["-creation_date"]