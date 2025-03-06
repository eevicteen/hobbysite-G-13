from django.db import models
from django.urls import reverse

# Create your models here.

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(_("Description"))
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, related_name='recipe')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=101)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')