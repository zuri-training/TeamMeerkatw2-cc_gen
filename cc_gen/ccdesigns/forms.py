from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from designs.models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'comment-field', 
        'rows': '2',
        'placeholder': 'Leave a comment...',
        }), label='')

    class Meta:
        model = Comment
        fields = ['body', ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
