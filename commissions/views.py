"""Receives web requests and returns the necessary web response."""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Commission, Job, JobApplication
from .forms import CommissionCreateForm, JobApplicationForm, CommissionEditForm, JobCreateForm


class CommissionListView(ListView):
    """Return commission_list html file with apt context."""
    model = Commission
    template_name = "commission_list.html"
    ordering = ["status", "-created_on"]

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
    job_application = 0

    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_id = request.POST.get("job_id")
            job_application.job = get_object_or_404(Job, id=job_id)
            job_application.applicant = request.user.profile
            job_application.save()
            return redirect('/commissions/detail/' + str(commission.pk))
    jobs = Job.objects.filter(commission=commission)
    applicants = JobApplication.objects.filter(job__in=jobs)
    people_required = 0
    for job in jobs:
        people_required += job.manpower_required
    accepted = 0
    applicant_number = 0
    for applicant in applicants:
        applicant_number += 1
        if applicant.status == 'b_accepted':
            accepted += 1
    open_slots = people_required - accepted
    ctx = {
        "commission": commission,
        "jobs": jobs,
        "people_required": people_required,
        "open_slots": open_slots,
        "applicants": applicants,
        "applicant_number": applicant_number
    }
    return render(request, "commission_detail.html", ctx)


@login_required
def create_commission(request):
    """Return commission_create html file with apt context."""
    commission_form = CommissionCreateForm()
    job_form1 = JobCreateForm()
    if request.method == 'POST':
        commission_form = CommissionCreateForm(request.POST)
        job_form1 = JobCreateForm(request.POST or None)
        if all([commission_form.is_valid(), job_form1.is_valid()]):
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            commission.save()
            job1 = job_form1.save(commit=False)
            job1.commission = commission
            job1.save()
            return redirect('/commissions/list', pk=commission.pk)
    ctx = {
        "commission_form": commission_form,
        "job_form1": job_form1,
    }
    return render(request, 'commission_create.html', ctx)


@login_required
def edit_commission(request, pk):
    """Return commission_edit html file with apt context."""
    commission = get_object_or_404(Commission, pk=pk)
    commission_form = CommissionEditForm(instance=commission)
    jobs = Job.objects.filter(commission=commission)
    applicants = JobApplication.objects.filter(job__in=jobs)
    people_required = 0
    for job in jobs:
        people_required += job.manpower_required
    accepted = 0
    for applicant in applicants:
        if applicant.status == 'b_accepted':
            accepted += 1
    open_slots = people_required - accepted
    if accepted >= people_required:
        commission.status = 'b_full'
        commission.save()
    ctx = {
        "commission_form": commission_form,
        "commission": commission,
        "jobs": jobs,
        "people_required": people_required,
        "open_slots": open_slots,
        "applicants": applicants
    }
    if request.method == 'POST':
        commission_form = CommissionEditForm(request.POST, instance=commission)
        if commission_form.is_valid():
            commission = commission_form.save(commit=False)
            commission.author = request.user.profile
            if open_slots < 1:
                commission.status = 'b_full'
            commission.save()
        return render(request, "commission_detail.html", ctx)

    ctx = {"commission_form": commission_form, "commission": commission}
    return render(request, "commission_edit.html", ctx)
