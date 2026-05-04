from django.db import models

class GeneratedImage(models.Model):
    prompt = models.CharField(max_length=255)
    image = models.ImageField(upload_to='generated/')
    created_at = models.DateTimeField(auto_now_add=True)