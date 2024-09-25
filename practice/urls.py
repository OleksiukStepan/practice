"""URL patterns for practice project."""

from django.urls import path

from practice.views import (
    index,
    TaskList,
    # TaskCreate,
)

urlpatterns = [
    path("", index, name="home"),
    path("tasks/", TaskList.as_view(), name="task_list"),
    # path("tasks/create", TaskCreate.as_view(), name="task_create"),
]

app_name = "practice"
