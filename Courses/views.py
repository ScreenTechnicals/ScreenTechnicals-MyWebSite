from multiprocessing import context
from django.shortcuts import render
from Courses.models import Playlist, Video
# Create your views here.

def courses(request):
    allCourses = Playlist.objects.all()
    if allCourses.exists():
        for playlist in allCourses:
            first_video = playlist.videos.all().first()
            slugOfFirstVideo = first_video.slug
    else:
        slugOfFirstVideo = ""


    context = {
        'allCourses':allCourses,
        'slugOfFirstVideo': slugOfFirstVideo,
    }
    return render(request, "Courses/courses.html", context)
    

def video(request, slug1, slug2):
    video_details = Video.objects.filter(slug=slug2).first()
    playlist = Playlist.objects.filter(slug=slug1).all()
    for video_s in playlist:
        vid = video_s.videos.all()
    playlist_slug = slug1
    current_playlist_name = playlist.first().playlist_name 
    context = {
        'video_details': video_details,
        'vid':vid,
        'playlist_slug': playlist_slug,
        'current_playlist_name':current_playlist_name,
    }
    return render(request, "Courses/video.html", context)

