from django.db import models

# Create your models here.
class PostType(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class post(models.Model):
    type = models.ManyToManyField(PostType)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/',default='default.png')
    discription = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title