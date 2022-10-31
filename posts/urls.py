from django.urls import path
from .views import http_post,http_services_single

app_name="posts"

urlpatterns = [
    path("post/1",http_post,name='post'),
    path("service-<str:s_id>",http_services_single,name='service_single'),


]
