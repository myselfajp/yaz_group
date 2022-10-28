from django.contrib import admin
from .models import post , PostType
# Register your models here.
admin.site.register(PostType)
admin.site.register(post)

