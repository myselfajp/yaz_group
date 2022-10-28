from django.urls import path
from .views import http_index,http_aboup_us

app_name="mysite"

urlpatterns = [
    path("",http_index,name='index'),
    path("about_us",http_aboup_us,name='about_us'),
]
