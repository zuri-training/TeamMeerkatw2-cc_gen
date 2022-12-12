from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUSer, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.homePage, name='home'),
    
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='ccdesigns\password-reset\password_reset.html',
             subject_template_name='ccdesigns/password-reset/password_reset_subject.txt',
             email_template_name='ccdesigns/password-reset/password_reset_email.html',
         ),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='ccdesigns\password-reset\password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='ccdesigns/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='ccdesigns/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]