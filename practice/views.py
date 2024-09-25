from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from practice.forms import TaskForm
from practice.models import Task


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(
        request, "pages/home.html", {"tasks": tasks}
    )


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "pages/task_form.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-created_at"]
    success_url = reverse_lazy("practice:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "pages/task_form.html"





