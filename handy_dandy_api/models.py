from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class User(models.Model):
    sid = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)

    # home_areas = []
    # home_area = []
    # task = []

    def __str__(self):
        return self.name


class HomeArea(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    notes = models.TextField(default='')
    # tasks = []
    # appliances = []


class Task(models.Model):
    name = models.CharField(max_length=64)
    appliance = models.CharField(max_length=32)
    category = models.CharField(max_length=24)
    description = models.TextField(default='')
    diy_links = models.TextField(default='')
    period_months = models.IntegerField()
    last_performed = models.DateField()


class Appliance(models.Model):
    name = models.CharField(max_length=32)
    model = models.CharField(max_length=128)
    serial_number = models.CharField(max_length=128)
