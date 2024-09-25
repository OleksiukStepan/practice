"""URL patterns for practice project."""

from django.urls import path

from practice.views import index

urlpatterns = [
    path("", index, name="home"),
]

app_name = "practice"
