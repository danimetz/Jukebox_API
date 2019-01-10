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

class TrackListCreate(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

def index(request):
    # import pdb; pdb.set_trace();
    return HttpResponse('Access Token:' + request.session['token_info']['access_token'])


def spotify_callback(request):
    SCOPE = 'user-library-read playlist-modify-public'
    sp_oauth = oauth2.SpotifyOAuth(
        settings.SPOTIPY_CLIENT_ID,
        settings.SPOTIPY_CLIENT_SECRET,
        settings.SPOTIPY_REDIRECT_URI,
        scope=SCOPE
        )

    if 'code' in request.GET:
        code = request.GET['code']
        token_info = sp_oauth.get_access_token(code)
        # import pdb; pdb.set_trace();
        request.session['token_info'] = token_info
        return HttpResponseRedirect('/')
    return HttpResponseRedirect(sp_oauth.get_authorize_url())

def playlists(request):
    sp = spotipy.Spotify(request.session['token_info']['access_token'])
    user = sp.current_user()
    playlists = sp.user_playlists(user['id'])

    return JsonResponse(playlists)
# displays search results

def select_playlist(request):
    return HttpResponse('ok')

def search(request):
    # import pdb; pdb.set_trace();
    sp = spotipy.Spotify(request.session['token_info']['access_token'])
    user = sp.current_user()
    q = request.GET['q']
    type = request.GET['type']
    searchResults = sp.search(q,20,0,type)

    return JsonResponse(searchResults)
