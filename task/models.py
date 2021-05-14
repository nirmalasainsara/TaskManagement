from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    duration = models.DateTimeField()
    image = models.ImageField()


class Task(models.Model):
    assign = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="task_assign"
    )
    reporter = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name="task_reporter"
    )
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    taskname = models.CharField(max_length=300)
    taskdescription = models.TextField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
