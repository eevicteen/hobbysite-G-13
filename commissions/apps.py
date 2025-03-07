"""Create app Commissions."""

from django.apps import AppConfig


class CommissionsConfig(AppConfig):
    """Create app Commissions and assign name and details."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commissions'
