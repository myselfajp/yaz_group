from django.urls import path
from .views import http_base,http_base2

app_name="posts"

urlpatterns = [
    path("post/1",http_base,name='base'),
    path("post/2",http_base2,name='base'),

]
