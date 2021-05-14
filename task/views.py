from django.shortcuts import render, redirect, reverse
from .models import Projects, Task
from .forms import ProjectForm, TaskForm
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def project_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("task:home"))

    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "task/project.html", context)


def home_view(request):
    project = Projects.objects.all()
    context = {"project": project}
    return render(request, "task/home.html", context)


@login_required
def task_create(request, project_id):
    project = Projects.objects.get(id=project_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            assign = form.cleaned_data.get("assign")
            taskname = form.cleaned_data.get("taskname")
            taskdescription = form.cleaned_data.get("taskdescription")
            startdate = form.cleaned_data.get("startdate")
            enddate = form.cleaned_data.get("enddate")
            task = Task.objects.create(
                project=project,
                reporter=request.user,
                assign=assign,
                taskname=taskname,
                taskdescription=taskdescription,
                startdate=startdate,
                enddate=enddate,
            )
            return redirect(reverse("task:home"))

    else:
        form = TaskForm()
    context = {"form": form, "project": project}
    return render(request, "task/task_create.html", context)
