from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/',default='default.png')
    discription = models.TextField()
    facebook = models.CharField(max_length=255,default='#')
    instagram = models.CharField(max_length=255,default='#')
    linkdin = models.CharField(max_length=255,default='#')
    whatsapp = models.CharField(max_length=255,default='#')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Uzmanlar"

class Projects(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects/',default='default.png')
    discription = models.TextField()
    reference = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Projeler"

class Services(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/',default='default.png')
    discription = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Hizmetler"

class Gallery(models.Model):
    name = models.CharField(max_length=255,null=True)
    project = models.ManyToManyField(Projects)
    image = models.ImageField(upload_to='projects/')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Galeri"

class References(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='references/',null=True)
    discription = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Referanslar"