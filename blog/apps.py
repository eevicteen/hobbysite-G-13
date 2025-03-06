"""Create app Blog."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Create app Blog and assign name and details."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
