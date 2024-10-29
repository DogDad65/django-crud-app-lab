# bikecollector/urls.py
from django.contrib import admin
from django.urls import path, include
from my_app import views  # Make sure 'my_app' matches your actual app name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # Homepage route
    path("bikes/", include("my_app.urls")),  # Include bike-related URLs from 'my_app'
]
