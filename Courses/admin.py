from django.contrib import admin

from Courses.models import Playlist, Video

# Register your models here.

admin.site.register(Playlist)
admin.site.register(Video)