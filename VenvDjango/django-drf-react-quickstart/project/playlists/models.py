from django.db import models

# Create your models here.
class Playlist(models.Model):
    user_id = models.CharField(max_length=100)
    playlist_id = models.CharField(max_length=100)
    access_token = models.CharField(max_length=300)
