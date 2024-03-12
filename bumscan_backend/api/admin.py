
from django.contrib import admin
from .models import Exercise, ExerciseGroup, Muscle


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['primary_muscle', 'secondary_muscle']


class ExerciseGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class MuscleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Muscle, MuscleAdmin)
admin.site.register(ExerciseGroup,ExerciseGroupAdmin)
