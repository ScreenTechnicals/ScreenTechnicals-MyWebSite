import email
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from Home.models import Contact
from Courses.models import Playlist
from Blog.models import BlogPost

# Create your views here.


def home(request):
    playlists = Playlist.objects.all()
    last = playlists[int(len(playlists)-1)]
    sec_last = playlists[int(len(playlists)-2)]
    th_last = playlists[int(len(playlists)-3)]
    blogs = BlogPost.objects.all()
    b_last = blogs[int(len(blogs)-1)]
    b_sec_last = blogs[int(len(blogs)-2)]
    context = {
        'last': last,
        'sec_last':sec_last,
        'th_last':th_last,
        'b_last':b_last,
        'b_sec_last':b_sec_last,
    }
    return render(request, 'Home/index.html', context)

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        if request.user.is_authenticated:
            if request.user.email == email:    
                contact = Contact(full_name=full_name, email=email, message=message)
                contact.save()
                messages.success(request, "Message Sent Successfully!")
                return redirect("contact")
            else:
                messages.success(request, "Please Enter Your registered email address!")
                return redirect("contact")

        else:
            messages.warning(request, "Please login To Send Messages!")
            return redirect("login")


    return render(request, 'Home/contact.html')
