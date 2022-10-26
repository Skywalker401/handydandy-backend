from rest_framework import serializers
from .models import User, Task, Competencies


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task


class CompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Competencies
