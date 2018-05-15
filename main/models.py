from django.db import models

# Create your models here.
class Gates (models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    repost = models.BooleanField()

