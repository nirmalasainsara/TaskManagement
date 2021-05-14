from django import forms

from .models import Projects, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = (
            "name",
            "description",
            "duration",
            "image",
        )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "assign",
            "taskname",
            "taskdescription",
            "startdate",
            "enddate",
        )
