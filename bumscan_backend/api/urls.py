from django.urls import path
from .views import ExerciseDetailView, ExerciseGroupDetailView

urlpatterns = [
    path("exercise/<slug:slug>/", ExerciseDetailView.as_view(), name="exercise-detail"),
    path("exercise-group/<slug:slug>/", ExerciseGroupDetailView.as_view(), name="exercise-group-detail")
]

