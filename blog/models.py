from django.db import models
from django.urls import reverse


# Create your models here.
class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]

    
class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    most_recent_update_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', args=[self.pk])
    
    class Meta:
        ordering = ["-creation_date"]
    