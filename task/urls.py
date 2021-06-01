from django.urls import path
from . import apiviews
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "task"

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("project/", views.project_view, name="project"),
    path(
        "project_detail/<int:project_id>/",
        views.project_detail_view,
        name="project_detail",
    ),
    path(
        "project_detail/<int:project_id>/task_create/",
        views.task_create,
        name="task_create",
    ),
    path(
        "project_detail/<int:project_id>/task_create/<int:task_id>/",
        views.task_detail_view,
        name="task_detail",
    ),
    path("reporter_task/", views.reporter_task_view, name="reporter_task"),
    path("assign_task/", views.assign_task_view, name="assign_task"),
    path("update/<int:project_id>/", views.update_project, name="update"),
    path("delete/<int:project_id>/", views.delete_project, name="delete"),
    path("register/", apiviews.RegisterView.as_view(), name="Register"),
    path("create/", apiviews.ProjectView.as_view(), name="create"),
    path(
        "projectdetail/<int:id>/",
        apiviews.ProjectDetailView.as_view(),
        name="projectdetail",
    ),
    path(
        "projectdetail/<int:project_id>/taskcreate/",
        apiviews.TaskCreateView.as_view(),
        name="taskcreate",
    ),
    path(
        "projectdetail/<int:project_id>/taskcreate/<int:task_id>/",
        apiviews.TaskDetailView.as_view(),
        name="taskcreate",
    ),
]
