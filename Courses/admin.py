from django.contrib import admin

from Courses.models import Playlist, Reply, Video, Comment

# Register your models here.

admin.site.register(Playlist)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Reply)
