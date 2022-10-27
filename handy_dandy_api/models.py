from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class User(models.Model):
    sid = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    email = models.EmailField(default='')
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    is_pro = models.BooleanField(default=False)

    # task_set = () foriegn keys of all tasks that have their owner assigned to this user (Automatically generated.
    # This feild exists without manual creation One-to-Many relation. Accessing owned tasks: "user.task_set.all()" and
    # 'user.appliance_set.all()". Another way is this: Task.objects.filter(owner_id=[the user's id])

    # competencies = {...}
    # reference with user.competencies. One-to-one relation

    def __str__(self):
        return self.name


class Competencies(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True)
    hvac = models.BooleanField(default=False)
    electrical = models.BooleanField(default=False)
    carpentry = models.BooleanField(default=False)
    plumbing = models.BooleanField(default=False)


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    is_complete = models.BooleanField(default=False)
    category = models.CharField(max_length=24)
    description = models.TextField(default='')
    period_months = models.CharField(max_length=12)
    last_performed = models.DateField()

    # Add more later
