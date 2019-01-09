from tracks.models import Track
from tracks.serializers import TrackSerializer
from rest_framework import generics
from django.shortcuts import render_to_response

from .models import Track
from .serializers import TrackSerializer
import spotipy
from spotipy import oauth2
import spotipy.util as util
import sys
import pprint

class TrackListCreate(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

# Create your views here.
