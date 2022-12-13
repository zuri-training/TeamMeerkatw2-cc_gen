from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfilUpdateForm, UserUpdateForm
# Create your views here.


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile-page')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
