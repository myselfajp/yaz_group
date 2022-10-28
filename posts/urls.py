from django.urls import path
from .views import http_post

app_name="posts"

urlpatterns = [
    path("post/1",http_post,name='post'),
]
