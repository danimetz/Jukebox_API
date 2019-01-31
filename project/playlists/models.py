import uuid
from django.db import models

# Create your models here.
class Playlist(models.Model):
    url = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    playlist_id = models.CharField(max_length=100)
    access_token = models.CharField(max_length=300)
    room_code = models.CharField(max_length=6)
