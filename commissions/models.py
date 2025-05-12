"""Create models Commission and Comments with appropriate fields."""

from django.db import models
from django.urls import reverse

# Create your models here.


class Commission(models.Model):
    """Create Commission with appropriate field, sorted by time created sorted ascendingly."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the title of the Commission."""

        return self.title

    def get_absolute_url(self):
        """Return the url of the Commission."""

        return reverse('commissions:commission-detail', args=[self.pk])

    class Meta:
        """Orders Commission by time created ascendingly."""

        ordering = ["created_on"]


class Comments(models.Model):
    """Create Comments with appropriate field, sorted by time created sorted ascendingly."""

    entry = models.TextField()
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Orders Comments by time created ascendingly."""
        
        ordering = ["-created_on"]

class Job(models.Model):
    """Create Jobs with appropriate field, sorted by status (Open > Full), manpower required, 
    in descending order, then role, in ascending order"""
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
    )
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveBigIntegerField()
    STATUS_CHOICES = [
        ('a_open', 'Open'),
        ('b_full', 'Full'),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='a_open')
    class Meta:
        """Orders Jobs by status (Open > Full), manpower required, in descending order, then role, in ascending order"""
        
        ordering = ["status","-manpower","role"]
