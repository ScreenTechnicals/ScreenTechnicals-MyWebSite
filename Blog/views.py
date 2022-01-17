from multiprocessing import context
from django.shortcuts import render
from Blog.models import BlogPost
# Create your views here.


def blogs(request):
    allBlogPosts = BlogPost.objects.all()
    context = {
        'allBlogPosts': allBlogPosts,
    }
    return render(request, "Blog/blogs.html", context)

def post(request, slug):
    post_details = BlogPost.objects.filter(slug=slug).first()
    context = {
        'post_details': post_details,
    }
    return render(request, "Blog/post.html", context)
