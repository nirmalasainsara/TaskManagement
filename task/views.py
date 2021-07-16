from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from .models import Projects, Task
from .forms import LoginForm, ProjectForm, SignUpForm, TaskForm
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# create project
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


# List of projects on home page
def home_view(request):
    project = Projects.objects.all()
    context = {"project": project}
    return render(request, "task/home.html", context)


# particular project detail when click on project_link
def project_detail_view(request, project_id):
    project = Projects.objects.get(id=project_id)
    tasks = Task.objects.filter(project=project)
    context = {"project": project, "tasks": tasks}
    return render(request, "task/project_detail.html", context)


# create task for a particular project
# @login_required
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
            return redirect(
                reverse(
                    "task:task_detail",
                    kwargs={"task_id": task.id, "project_id": project_id},
                )
            )

    else:
        form = TaskForm()
    context = {"form": form, "project": project}
    return render(request, "task/task_create.html", context)


# check task detail
def task_detail_view(request, task_id, project_id):
    task = Task.objects.get(id=task_id)
    context = {"task": task}
    return render(request, "task/task_detail.html", context)


@login_required
def reporter_task_view(request):
    tasks = Task.objects.filter(reporter=request.user)
    context = {"tasks": tasks}
    return render(request, "task/reporter_task.html", context)


def assign_task_view(request):
    tasks = Task.objects.filter(assign=request.user)
    context = {"tasks": tasks}
    return render(request, "task/assign_task.html", context)


def delete_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    project.delete()
    return redirect(reverse("task:home"))


def update_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    form = ProjectForm(request.POST, instance=project)
    if form.is_valid():
        form.save()
        return redirect(reverse("task:home"))
    return render(request, "task/project.html", {"project": project, "form": form})


def signup_view(request):
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect(reverse("task:home"))

    context = {"form": form}
    return render(request, "task/project.html", context)


# user login page
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse("task:home"))
    return render(request, "task/project.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect(reverse("task:home"))
