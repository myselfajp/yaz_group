from .views import *
from django.urls import path
from .views import http_base

app_name="mysite"

urlpatterns = [
    path("",http_base,name='base'),
    
]
