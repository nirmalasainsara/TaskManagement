from rest_framework import serializers
from .models import Projects, Task
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "email")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
            validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    assign_name = serializers.SerializerMethodField()
    reporter_name = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            "assign_name",
            "reporter_name",
            "taskname",
            "taskdescription",
            "startdate",
            "enddate",
        )

    def create(self, validated_data):
        print(validated_data)
        return Task.objects.create(**validated_data)

    def get_assign_name(self, obj):
        return obj.assign.username

    def get_reporter_name(self, obj):
        return obj.reporter.username
