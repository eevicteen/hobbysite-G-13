"""Create models Commission and Comments with appropriate fields."""

from django.db import models
from django.urls import reverse

from user_management.models import Profile


class Commission(models.Model):
    """Create Commission with appropriate field, sorted by time created sorted ascendingly."""

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    STATUS_CHOICES = [
        ('a_open', 'Open'),
        ('b_full', 'Full'),
        ('c_completed', 'Completed'),
        ('d_discontinued', 'Discontinued'),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='a_open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the title of the Commission."""

        return self.title

    def get_absolute_url(self):
        """Return the url of the Commission."""

        return reverse('commissions:commission-detail', args=[self.pk])

    def get_status(self, status):
        """"return status of the Commission."""
        return status

    class Meta:
        """Orders Commission by time created ascendingly."""

        ordering = ["created_on"]


class Job(models.Model):
    """Create Jobs with appropriate field, sorted by status (Open > Full), manpower 
    required, in descending order, then role, in ascending order"""
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

    def __str__(self):
        """Return the role of the Job."""
        return self.role

    def get_commission(self):
        return self.commission

    class Meta:
        """Orders Jobs by status (Open > Full), manpower required, 
        in descending order, then role, in ascending order"""

        ordering = ["status", "-manpower_required", "role"]


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,)
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    STATUS_CHOICES = [
        ('a_pending', 'Pending'),
        ('b_accepted', 'Accepted'),
        ('c_rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='a_pending')

    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Orders Jobs by status (Open > Full), manpower required, 
        in descending order, then role, in ascending order"""

        ordering = ["status", "-applied_on"]
