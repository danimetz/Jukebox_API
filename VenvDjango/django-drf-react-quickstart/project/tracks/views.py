from tracks.models import Track
from tracks.serializers import TrackSerializer
from rest_framework import generics
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.apps import apps
from .models import Track
from playlists.models import Playlist

from .serializers import TrackSerializer
import spotipy
from spotipy import oauth2
import spotipy.util as util
import sys
import pprint
from django.conf import settings


def index(request):
    return HttpResponseRedirect("http://ada-jukebox.herokuapp.com/")

def spotify_callback(request):
    SCOPE = 'user-library-read playlist-modify-public'
    sp_oauth = oauth2.SpotifyOAuth(
        settings.SPOTIPY_CLIENT_ID,
        settings.SPOTIPY_CLIENT_SECRET,
        settings.SPOTIPY_REDIRECT_URI,
        scope=SCOPE
        )
    if 'code' in request.GET:
        print("Spotify Callback")
        code = request.GET['code']
        token_info = sp_oauth.get_access_token(code)
        # import pdb; pdb.set_trace();

        try:
            return HttpResponseRedirect("http://ada-jukebox.herokuapp.com/?access_token=" + token_info['access_token'])
        except StandardError as e:
            print(e)
            return

    return HttpResponseRedirect(sp_oauth.get_authorize_url())

def playlists(request):
    token = request.META['HTTP_X_SPOTIFY_TOKEN']
    sp = spotipy.Spotify(token)
    user = sp.current_user()
    playlists = sp.user_playlists(user['id'])

    return JsonResponse(playlists)
# displays search results
def playlist(request):

    if 'room_code' in request.GET:
        room_code = request.GET['room_code']
        current_playlist = Playlist.objects.get(room_code__exact=room_code)
        print(current_playlist)
        sp = spotipy.Spotify(current_playlist.access_token)
        user = sp.current_user()
        playlist_tracks = sp.user_playlist_tracks(user['id'], playlist_id=current_playlist.playlist_id)
        print(playlist_tracks)
    else:
        token = request.META['HTTP_X_SPOTIFY_TOKEN']
        sp = spotipy.Spotify(token)
        user = sp.current_user()
        playlist_tracks = sp.user_playlist_tracks(user['id'], playlist_id=request.GET['playlist_id'])


    return JsonResponse(playlist_tracks)

def select_playlist(request):
    return HttpResponse('ok')

def search(request):
    # import pdb; pdb.set_trace();
    q = request.GET['q']
    type = request.GET['type']

    if 'room_code' in request.GET:
        room_code = request.GET['room_code']
        current_playlist = Playlist.objects.get(room_code__exact=room_code)
        sp = spotipy.Spotify(current_playlist.access_token)
    else:
        token = request.META['HTTP_X_SPOTIFY_TOKEN']
        sp = spotipy.Spotify(token)
        user = sp.current_user()

    searchResults = sp.search(q,20,0,type)

    return JsonResponse(searchResults)
