"""Receives web requests and returns the necessary web response."""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Commission,Comments


class CommissionListView(ListView):
    """Return commission_list html file with apt context."""
    
    model = Commission
    template_name = "commission_list.html"

def commission_detail(request, pk):
    """Return commission_detail html file with apt context."""
    
    commission = get_object_or_404(Commission, pk=pk)
    comments = Comments.objects.filter(commission=commission)

    ctx = {
        "commission": commission,
        "comments": comments
    }

    return render(request, "commission_detail.html", ctx)