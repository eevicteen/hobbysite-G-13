from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255)
    email_address = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.display_name