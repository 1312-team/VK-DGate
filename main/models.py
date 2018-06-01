from django.db import models

# Create your models here.
class Gate (models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    link = models.URLField()
    repost = models.BooleanField()

