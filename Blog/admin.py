from django.contrib import admin
from Blog.models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinymce.js',)

