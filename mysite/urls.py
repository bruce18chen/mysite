# mysite/urls.py

from django.contrib import admin
from django.urls import path

from . import views   # Import the views module

urlpatterns = [
    path('', views.index),  # Add our index view to the URL patterns
    path('admin/', admin.site.urls),
]