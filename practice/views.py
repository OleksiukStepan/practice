from django.shortcuts import render

from practice.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(
        request, "pages/home.html", {"tasks": tasks}
    )