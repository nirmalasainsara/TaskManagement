from datetime import datetime, timedelta
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
from .models import Projects, Task
from .serializers import (
    ProjectSerializer,
    TaskSerializer,
    RegisterSerializer,
    UserSerializer,
)
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from rest_framework.permissions import IsAuthenticated


# Register apiview
class RegisterView(generics.ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            create = serializer.save()
            serializer = RegisterSerializer(create)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# project apiview
class ProjectView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            img = request.FILES.get("image")
            fs = FileSystemStorage()
            image = fs.save(img.name, img)
            create = serializer.save(image=image)
            serializer = ProjectSerializer(create)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# project detail apiview
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    lookup_url_kwarg = "id"
    queryset = Projects.objects.all()


# Task apiView
class TaskCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        project_id = self.kwargs.get("project_id")
        project = Projects.objects.get(id=project_id)
        return Task.objects.filter(project=project)

    def post(self, request, *args, **kwargs):
        project_id = self.kwargs.get("project_id")
        assign_id = self.request.query_params.get("assign_id")
        project = Projects.objects.get(id=project_id)
        assign = User.objects.get(id=assign_id)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            create = serializer.save(
                project=project, assign=assign, reporter=request.user
            )
            serializer = TaskSerializer(create)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Task detail apiview
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_url_kwarg = "task_id"
    queryset = Task.objects.all()
