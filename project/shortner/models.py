from django.db import models

# Create your models here.

class Shorturl(models.Model):
    short_url = models.CharField(blank=False, max_length=20)
    long_url = models.URLField("URL",unique=True)
