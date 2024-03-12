
from django.db import models
from django.utils.text import slugify
import os
import uuid


def image_file_path(instance, filename):
    """Generate file path for user avatar"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("pictures", filename)


class Muscle(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='عنوان', blank=False, null=False)
    slug = models.SlugField(unique=True, blank=True, null=True)

    image = models.ImageField(upload_to=image_file_path, null=True, blank=True, verbose_name='عکس')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)


class Exercise(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='عنوان', blank=False, null=False)
    primary_muscle = models.ForeignKey('Muscle', on_delete=models.CASCADE, related_name='primary_muscle')
    secondary_muscle = models.ForeignKey('Muscle', on_delete=models.CASCADE, related_name='secondary_muscle')
    instructions = models.TextField(null=False, blank=False, verbose_name='دستورالعمل')

    first_image = models.ImageField(upload_to=image_file_path, null=True, blank=True, verbose_name='عکس و فایل')
    second_image = models.ImageField(upload_to=image_file_path, null=True, blank=True, verbose_name='عکس و فایل')
    third_image = models.ImageField(upload_to=image_file_path, null=True, blank=True, verbose_name='عکس و فایل')

    first_str_lvl = models.IntegerField(help_text='kg')
    second_str_lvl = models.IntegerField(help_text='kg')
    third_str_lvl = models.IntegerField(help_text='kg')
    fourth_str_lvl = models.IntegerField(help_text='kg')
    fifth_str_lvl = models.IntegerField(help_text='kg')

    def __str__(self):
        return self.name

    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)


class ExerciseGroup(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='عنوان گروه')
    related_exercises = models.ManyToManyField('Exercise')
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

