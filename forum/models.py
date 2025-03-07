from django.db import models
from django.urls import reverse

# Create your models here.

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        "Order the post categories alphabetically."
        ordering = ["name"]

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, related_name='recipe')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])
    