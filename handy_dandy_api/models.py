from django.contrib.auth import get_user_model
from django.db import models


class User(models.Model):
    sid = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    email = models.EmailField(default='')
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)
    # task_set = () foriegn keys of all tasks that have their owner assigned to this user
    # appliance_set = () same as above but appliances

    def __str__(self):
        return self.name

    # I don't think we need these helped functions below and I think they're awful syntax anyways. I think we have
    # access elsewhere via "user.task_set.all()" and 'user.appliance_set.all()". leaving this here for now just in
    # case we do need something like this.
    # Another way is this: Task.objects.filter(owner_id=[the user's id])

    # def get_tasks(self):
    #     if self.task_set:
    #         return [Task.objects.filter(pk=task) for task in self.task_set]
    #     else:
    #         return None
    #
    # def get_appliances(self):
    #     if self.appliance_set:
    #         return [Appliance.objects.get(pk=appliance) for appliance in self.appliance_set]
    #     else:
    #         return None


class Task(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    appliance = models.CharField(max_length=32)
    home_area = models.CharField(max_length=24)
    description = models.TextField(default='')
    diy_links = models.TextField(default='')
    period_months = models.IntegerField()
    last_performed = models.DateField()


class Appliance(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    model = models.CharField(max_length=128)
    serial_number = models.CharField(max_length=128)
