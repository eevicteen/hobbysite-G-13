"""Receives web requests and returns the necessary web response."""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Commission,Comments, Job, JobApplication
from .forms import CommissionCreateForm, JobApplicationForm, CommissionEditForm


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

@login_required
def commission_detail(request, pk):
    """Return commission_detail html file with apt context."""
    
    commission = get_object_or_404(Commission, pk=pk)
    job_application = 0

    comments = Comments.objects.filter(commission=commission)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_id = request.POST.get("job_id")
            job_application.job = get_object_or_404(Job, id=job_id)
            print(job_application.job)
            job_application.applicant = request.user.profile
            job_application.save()
    
            return redirect('/commissions/detail/' + str(commission.pk))
    jobs = Job.objects.filter(commission=commission)
    applicants = JobApplication.objects.filter(job__in=jobs)
    people_required = 0
    for job in jobs:
        people_required += job.manpower_required
    accepted = 0
    for applicant in applicants:
        if applicant.status == 'b_accepted':
            accepted +=1
    open_slots = people_required - accepted
    ctx = {
                "commission": commission,
                "comments": comments,
                "jobs": jobs,
                "people_required":people_required,
                "open_slots": open_slots,
                "applicants": applicants
            }
    return render(request, "commission_detail.html", ctx)

#@login_required
def create_commission(request):
    form = CommissionCreateForm()
    if request.method == 'POST':
        form = CommissionCreateForm(request.POST)
    if form.is_valid():
        commission = form.save(commit=False)
        commission.author = request.user.profile
        commission.save()
        return redirect('/commissions/list', pk=commission.pk)
    ctx = {"form": form}
    return render(request, 'commission_create.html', ctx)

@login_required
def edit_commission(request,pk):
    commission = get_object_or_404(Commission, pk=pk)
    form = CommissionEditForm()
    jobs = Job.objects.filter(commission=commission)
    applicants = JobApplication.objects.filter(job__in=jobs)
    people_required = 0
    for job in jobs:
        people_required += job.manpower_required
    accepted = 0
    for applicant in applicants:
        if applicant.status == 'b_accepted':
            accepted +=1
    open_slots = people_required - accepted
    ctx = {
                "commission": commission,
                "jobs": jobs,
                "people_required":people_required,
                "open_slots": open_slots,
                "applicants": applicants
            }
    if request.method == 'POST':
        form = CommissionEditForm(request.POST, instance=commission)
        # if form.is_valid():
        #     updated_commission = form.save(commit=False)
        #     if updated_commission.owner != request.user.profile:
        #         return render(request, 'product_detail.html', {
        #             'form': form,
        #             'commission': commission,
        #             'error_message': "You are not authorized to edit this product."
        #         })
        #     updated_commission.status = 'out_of_stock' if updated_product.stock == 0 else 'available'
        #     updated_commission.save()
        #     return redirect('commission:commission-detail', pk=commission.pk)
    else:
        form = CommissionEditForm(instance=commission)

    ctx = {"form": form, "commission":commission}
    # return render(request, 'product_create.html', ctx)
    return render(request, "commission_edit.html", ctx)


