from tracks.models import Track
from tracks.serializers import TrackSerializer
from rest_framework import generics
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from .models import Track
from .serializers import TrackSerializer
import spotipy
from spotipy import oauth2
import spotipy.util as util
import sys
import pprint
from django.conf import settings


def index(request):
    return HttpResponseRedirect("https://ada-jukebox.herokuapp.com/")

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
        request.session['token_info'] = token_info

        print(token_info)
        try:
            return HttpResponseRedirect("https://ada-jukebox.herokuapp.com/?access_token=" + token_info['access_token'])
        except StandardError as e:
            print(e)
            return

    return HttpResponseRedirect(sp_oauth.get_authorize_url())

def playlists(request):
    # print(request)
    # print(request.session['token_info'])
    # sp = spotipy.Spotify(request.session['token_info']['access_token'])
    token = request.META['HTTP_X_SPOTIFY_TOKEN']
    sp = spotipy.Spotify(token)
    user = sp.current_user()
    playlists = sp.user_playlists(user['id'])

    return JsonResponse(playlists)
# displays search results
def playlist(request):
    # sp = spotipy.Spotify(request.session['token_info']['access_token'])
    token = request.META['HTTP_X_SPOTIFY_TOKEN']
    sp = spotipy.Spotify(token)
    user = sp.current_user()
    playlist_tracks = sp.user_playlist_tracks(user['id'], playlist_id=request.GET['playlist_id'])

    return JsonResponse(playlist_tracks)

def select_playlist(request):
    return HttpResponse('ok')

def search(request):
    # import pdb; pdb.set_trace();
    token = request.META['HTTP_X_SPOTIFY_TOKEN']

    sp = spotipy.Spotify(token)
    # sp = spotipy.Spotify(request.session['token_info']['access_token'])
    user = sp.current_user()
    q = request.GET['q']
    type = request.GET['type']
    searchResults = sp.search(q,20,0,type)

    return JsonResponse(searchResults)
