from rest_framework import serializers
from .models import ExerciseGroup, Exercise, Muscle


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = '__all__'
        depth = 1


class MuscleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Muscle
        fields = ['name', 'image']


class ExerciseGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseGroup
        fields = ['name', 'related_exercises']
        depth = 1


