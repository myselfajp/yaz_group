from django.urls import path
from .views import http_contact_us,http_quote

app_name="contact"


urlpatterns = [
    path("contact_us",http_contact_us,name='contact_us'),
    path("quote",http_quote,name='quote'),

]
