from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

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
    return render(request, 'ccdesigns/home.html')

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
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                
                login(request, user)
                return redirect('home')
        else:
            messages.info(request, 'Passwords do not match')
    context = {}
    return render(request, 'ccdesigns/register.html', context)