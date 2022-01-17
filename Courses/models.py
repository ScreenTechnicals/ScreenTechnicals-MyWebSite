from email.policy import default
from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Video(models.Model):
    video_name = models.CharField(max_length=100)
    video_url = models.URLField()
    overview = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='video_name',
                         unique=True, null=True, blank=True, default=None)
    def __str__(self):
        return f"{self.video_name}"
    

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="images/", blank=True, null=True, default=None)
    videos = models.ManyToManyField(Video, related_name="videos")
    desc = models.CharField(max_length=150, null=True, blank=True, default="")
    # date_time = models.DateTimeField()
    slug = AutoSlugField(populate_from='playlist_name',
                         unique=True, null=True, blank=True, default=None)

    
    def __str__(self):
        return self.playlist_name
    
