from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, blank=True, default=None)
    
    def __str__(self):
        return f"{self.title}-{self.category}"
    
