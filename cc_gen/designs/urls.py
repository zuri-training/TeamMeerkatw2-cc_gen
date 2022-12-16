from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.design_page, name='card-design'),
]
