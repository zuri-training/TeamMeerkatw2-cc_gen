from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilUpdateForm(forms.ModelForm):
    bio = forms.CharField(max_length=250, required=False, widget=forms.Textarea(attrs={'rows': '1','Type':'text'}))
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'phone_no']