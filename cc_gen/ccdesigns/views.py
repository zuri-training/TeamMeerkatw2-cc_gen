from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from designs.models import DesignInfo, Comment
import mimetypes

# Create your views here.

def card_detail(request, pk):
    design = DesignInfo.objects.get(id=pk)
    designs = DesignInfo.objects.all()[3:5]
    user = request.user
    comments = design.comment_set.all()
    
    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            design=design,
            body = request.POST.get('body'),
        )
        return redirect('card_detail', pk=design.id)


    context = {
        'comments': comments,
        'designs': designs,
        'design': design,
        'user': user,
    }
    return render(request, 'ccdesigns/card_detail.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR Password does not exist")
    return render(request, 'ccdesigns/login.html')


def logoutUSer(request):
    logout(request)
    return redirect('home')


def homePage(request):
    design = DesignInfo.objects.all()[:6]
    user = request.user

    context = {
        'design': design,
        'user': user
    }
    return render(request, 'ccdesigns/home.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST['Fname']
        last_name = request.POST['Lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exists!')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Exists!')
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()

                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
    context = {}
    return render(request, 'ccdesigns/register.html', context)

def about_page(request):
    return render(request, 'ccdesigns/about.html')

def contactPage(request):
    return render(request, 'ccdesigns/contact.html')


# def download_file(request):
#     # fill these variables with real values
#     fl_path = '
#     filename = ‘downloaded_file_name.extension’

#     fl = open(fl_path, 'r’)
#     mime_type, _ = mimetypes.guess_type(fl_path)
#     response = HttpResponse(fl, content_type=mime_type)
#     response['Content-Disposition'] = "attachment; filename=%s" % filename
#     return response
