"""Create app merchstore."""

from django.apps import AppConfig


class MerchstoreConfig(AppConfig):
    """Create merchstore and add name."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'merchstore'
