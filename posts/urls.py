from django.urls import path
from .views import http_services_single,http_gallery

app_name="posts"

urlpatterns = [
    path("service-<str:s_id>",http_services_single,name='service_single'),
    path("project-<str:s_id>",http_gallery,name='gallery'),

]
