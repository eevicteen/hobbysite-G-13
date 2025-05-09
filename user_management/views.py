from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ProfileForm, RegisterForm
from .models import Profile

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

@login_required
def profile_update(request, username):
    user = get_object_or_404(User, username=username)

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None 

    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
    else:
        form = ProfileForm(instance=profile)

    if form.is_valid():
        profile = form.save()
        profile.user = user 
        profile.save()
        return redirect('user_management:profile-update', username=username)
    
    ctx = {
        'form': form,
        'user': user,
        'profile': profile,
    }
    return render(request, 'profile_update.html', ctx)
