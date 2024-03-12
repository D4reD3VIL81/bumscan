
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ExerciseGroup, Exercise
from .serializers import ExerciseSerializer, ExerciseGroupSerializer
from django.shortcuts import get_object_or_404


class ExerciseDetailView(generics.RetrieveAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Exercise, slug=slug)


class ExerciseGroupDetailView(generics.RetrieveAPIView):
    queryset = ExerciseGroup.objects.all()
    serializer_class = ExerciseGroupSerializer

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(ExerciseGroup, slug=slug)
