from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']