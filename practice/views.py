from django.shortcuts import render
from django.views.generic import ListView

from practice.models import Task


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(
        request, "pages/home.html", {"tasks": tasks}
    )


class TaskList(ListView):
    model = Task
    template_name = "pages/task_list.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-created_at"]

