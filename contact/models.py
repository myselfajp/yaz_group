from django.db import models

# Create your models here.
class Message(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Mesajlar"

class Quote(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Başvurular"

