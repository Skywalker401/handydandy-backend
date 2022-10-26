from rest_framework import serializers
from .models import User, Task, Competencies


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task


class CompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('hvac', 'electrical', 'carpentry', 'plumbing')
        model = Competencies


class UserSerializer(serializers.ModelSerializer):
    competencies = CompetenciesSerializer()

    class Meta:
        fields = '__all__'
        model = User

    def create(self, validated_data):
        user = User.objects.create(
            **validated_data)
        Competencies.objects.create(owner=user,
                                    **validated_data["competencies"])
        return user
