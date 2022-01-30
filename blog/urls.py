from django.urls import path

from .models import *
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
]
