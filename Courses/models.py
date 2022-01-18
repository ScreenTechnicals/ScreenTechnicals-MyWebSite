from email.policy import default
from operator import imod
from django.db import models
from autoslug import AutoSlugField
from Accounts.models import Account
from django.contrib.auth.models import User

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
    

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class Reply(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

