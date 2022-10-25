from rest_framework import serializers
from .models import User, Task, Appliance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task


class ApplianceSerializer(serializers.ModelSerializer):
    class Meta:
        feilds = ('owner', 'name', 'model', 'serial_numer',)
        model = Appliance
