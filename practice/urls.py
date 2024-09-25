"""URL patterns for practice project."""

from django.urls import path

from practice.views import (
    index,
    TaskCreateView,
    # TagsListView,
)

urlpatterns = [
    path("", index, name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    # path("tags/", TagsListView.as_view(), name="tag_list"),
]

app_name = "practice"
