from django.db import models

class MyFile(models.Model):
    original = models.ImageField(blank=False, null=False)
    description = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.ImageField(blank=True)
