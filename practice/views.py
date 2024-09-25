from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from practice.forms import TaskForm, TagForm
from practice.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "pages/home.html"
    ordering = ["is_done", "-created_at"]

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        task = get_object_or_404(Task, id=task_id)

        if "Complete" in request.POST:
            task.is_done = True
            task.save()
        elif "Undo" in request.POST:
            task.is_done = False
            task.save()

        return redirect("practice:home")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "pages/task_form.html"
    success_url = reverse_lazy("practice:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "pages/task_form.html"
    success_url = reverse_lazy("practice:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "pages/confirm_delete.html"
    success_url = reverse_lazy("practice:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["name"] = "Task"
        context["success_url"] = self.success_url
        return context


class TagListView(ListView):
    model = Tag
    template_name = "pages/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "pages/tag_form.html"
    success_url = reverse_lazy("practice:tag_list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "pages/tag_form.html"
    success_url = reverse_lazy("practice:tag_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "pages/confirm_delete.html"
    success_url = reverse_lazy("practice:tag_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["name"] = "Tag"
        context["success_url"] = self.success_url
        return context
