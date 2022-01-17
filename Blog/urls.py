from django.urls import path
from Blog import views

urlpatterns = [
    path('blogs/', views.blogs, name="blogs"),
    path('blogs/<str:slug>/', views.post, name="post"),
]
