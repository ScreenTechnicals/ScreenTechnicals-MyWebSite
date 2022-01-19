from django.contrib import admin

from Courses.models import Playlist, Reply, Video, Comment

# Register your models here.

admin.site.register(Playlist)
admin.site.register(Comment)
admin.site.register(Reply)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinymce.js',)
