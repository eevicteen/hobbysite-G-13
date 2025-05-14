"""Receives web requests and returns the necessary web response."""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from .models import Commission,Comments, Job, JobApplication
from .forms import CommissionCreateForm


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

    # if request.method == 'POST':
    #     job_id = request.POST.get("job_id")
    #     job = get_object_or_404(Job, id=job_id)
    #     form = JobApplicationForm(request.POST)
    # if form.is_valid():
    #     job_application = form.save(commit=False)
    #     job_application.job = job
    #     job_application.applicant = request.user.profile
    #     commission.save()
    #     return redirect('/commissions/list', pk=commission.pk)


    ctx = {
        "commission": commission,
        "comments": comments,
        "jobs": jobs,
        "people_required":people_required,
        "open_slots": open_slots
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

#@login_required
# def edit_commission(request,pk):
#     product = get_object_or_404(Product, pk=pk)
#     form = ProductEditForm()
#     if request.method == 'POST':
#         form = ProductEditForm(request.POST, instance=product)
#         if form.is_valid():
#             updated_product = form.save(commit=False)
#             if updated_product.owner != request.user.profile:
#                 return render(request, 'product_detail.html', {
#                     'form': form,
#                     'product': product,
#                     'error_message': "You are not authorized to edit this product."
#                 })
#             updated_product.status = 'out_of_stock' if updated_product.stock == 0 else 'available'
#             updated_product.save()
#             return redirect('merchstore:product-detail', pk=product.pk)
#     else:
#         form = ProductEditForm(instance=product)

#     ctx = {"form": form, "product":product}
#     return render(request, 'product_create.html', ctx)

