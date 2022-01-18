from django.shortcuts import render, redirect
from Courses.models import Playlist, Video, Comment
from django.contrib import messages
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

    if request.method == "POST":
        current_user = request.user
        current_video = Video.objects.get(slug=slug2)
        comment_text = request.POST['comment_text']

        comment = Comment(user=current_user, video=current_video, text=comment_text)
        comment.save()
        messages.success(request, "Commented")
        return redirect(f"/courses/{playlist_slug}/{video_details.slug}/")

    current_playlist_name = playlist.first().playlist_name 
    allComments = Comment.objects.filter(video=video_details)
    print(allComments)
    context = {
        'video_details': video_details,
        'vid':vid,
        'playlist_slug': playlist_slug,
        'current_playlist_name':current_playlist_name,
        'allComments':allComments,
    }
    return render(request, "Courses/video.html", context)

