from django.urls import path
from .views import http_index,http_aboup_us,http_qoute,http_contact_us,http_projects,http_our_team,http_services
app_name="mysite"

urlpatterns = [
    path("",http_index,name='index'),
    path("about_us",http_aboup_us,name='about_us'),
    path("contact_us",http_contact_us,name='contact_us'),
    path("qoute",http_qoute,name='qoute'),
    path("projects",http_projects,name='projects'),
    path("services",http_services,name='services'),
    path("our_team",http_our_team,name='our_team'),

]
