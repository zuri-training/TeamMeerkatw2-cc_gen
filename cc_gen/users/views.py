from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfilUpdateForm, UserUpdateForm
from designs.models import DesignInfo
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    designs = DesignInfo.objects.all()[:2]
    context = {
        'user': user,
        'designs': designs,
    }
    return render(request, 'users/profile.html', context)

def updateProfile(request):
    user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile-page', pk=user.id)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update.html', context)
