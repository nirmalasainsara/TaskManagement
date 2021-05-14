from django.urls import path
from . import apiviews
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "task"

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("project/", views.project_view, name="project"),
    path(
        "task_create/<int:project_id>/",
        views.task_create,
        name="task_create",
    ),
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
