from django.contrib import admin
from .models import Photo, Video


@admin.register(Photo)
class Photo(admin.ModelAdmin):
    pass


@admin.register(Video)
class Video(admin.ModelAdmin):
    pass
