from django.urls import include, path
from . import views
urlpatterns = [
    path('profile/<str:pk>/', views.profile, name='profile-page'),
    path('update/', views.updateProfile, name='update'),
    
]
