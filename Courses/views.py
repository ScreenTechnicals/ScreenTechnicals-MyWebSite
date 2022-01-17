from multiprocessing import context
from django.shortcuts import render
from Courses.models import Playlist, Video
# Create your views here.

def courses(request):
    allCourses = Playlist.objects.all()
    fisrt_video = allCourses.first()
    slugOfFirstVideo = fisrt_video.videos.all().first().slug
    
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
    context = {
        'video_details': video_details,
        'vid':vid,
        'playlist_slug': playlist_slug,
    }
    return render(request, "Courses/video.html", context)

