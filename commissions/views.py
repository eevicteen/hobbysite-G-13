"""Receives web requests and returns the necessary web response."""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Commission,Comments, Job, JobApplication


class CommissionListView(ListView):
    """Return commission_list html file with apt context."""
    model = Commission
    template_name = "commission_list.html"
    ordering = ["status","-created_on"]

def commission_detail(request, pk):
    """Return commission_detail html file with apt context."""
    
    commission = get_object_or_404(Commission, pk=pk)
    comments = Comments.objects.filter(commission=commission)
    jobs = Job.objects.all()
    for x in jobs:
        print(jobs.role)
        print("break muna")
        print("break muna")
        print("break muna")

    ctx = {
        "commission": commission,
        "comments": comments
    }

    return render(request, "commission_detail.html", ctx)

class JobListView (ListView):
    model=Job
    context_object_name = "job_list"


def job_list(request):
    """Return commission_list html file with apt context."""

    jobs = Job.objects.all()
    job_applications = JobApplication.objects.all()

    ctx = {
        "jobs": jobs,
        "job_applications": job_applications
    }

    return render(request, "commission_list.html", ctx)