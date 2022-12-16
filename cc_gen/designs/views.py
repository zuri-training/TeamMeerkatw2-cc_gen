from django.shortcuts import render, redirect
from .models import Comment, Likes, DesignInfo 

# Create your views here.

def design_page(request):
    design = DesignInfo.objects.all()
    user = request.user
    
    context = {
        'design': design,
        'user': user
    }
    return render(request, 'designs/cards.html', context)


def like_post(request):
    return redirect('card-design')
