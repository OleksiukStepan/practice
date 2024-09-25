from django import forms
from practice.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
