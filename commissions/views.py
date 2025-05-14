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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commissions = Commission.objects.all()
        jobs = Job.objects.all()
        applications = JobApplication.objects.all()
        context["commissions"] = commissions
        context["jobs"] = jobs
        context["applications"] = applications
        return context


def commission_detail(request, pk):
    """Return commission_detail html file with apt context."""
    
    commission = get_object_or_404(Commission, pk=pk)
    comments = Comments.objects.filter(commission=commission)

    ctx = {
        "commission": commission,
        "comments": comments
    }

    return render(request, "commission_detail.html", ctx)

