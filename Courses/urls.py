from django.urls import path
from Courses import views

urlpatterns = [
    path('courses/', views.courses, name="courses"),
    path('courses/<str:slug1>/<str:slug2>/', views.video, name="video"),
]
