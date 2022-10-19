from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    zip = models.CharField(max_length=10)

    # home_areas = []
    # home_area = []
    # task = []

    def __str__(self):
        return self.name
