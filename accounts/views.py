from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import RegisterForm
from user_management.models import Profile

# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password']) 
        user.save()

        Profile.objects.create(
                user=user,
                display_name=user.username,
                email_address=user.email  
            )
        
        return redirect('login')
    ctx = {"form": form }
    return render(request, 'register.html', ctx)

