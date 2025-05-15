from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ProfileForm
from .models import Profile

@login_required
def profile_update(request, username):
    user = get_object_or_404(User, username=username)

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None 

    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
    else:
        form = ProfileForm( instance=profile)

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
