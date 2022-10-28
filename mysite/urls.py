from django.urls import path
from .views import http_index

app_name="mysite"

urlpatterns = [
    path("",http_index,name='index'),
]
