"""URL patterns for practice project."""

from django.urls import path

from practice.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
]

app_name = "practice"
