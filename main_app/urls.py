from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('photography', views.photography),
    path('photographers', views.photographers),
    path('likepicture/',views.like_photo, name='like_photo')
]