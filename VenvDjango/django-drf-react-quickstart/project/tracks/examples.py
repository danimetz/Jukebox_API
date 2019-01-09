from rest_framework import generics
from django.shortcuts import render_to_response

from .models import Twitterparse
from .serializers import TwitterparseSerializer

from twitter_auth.utils import *

class ListTwitterDataView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Twitterparse.objects.all()
    serializer_class = TwitterparseSerializer

def timeline(request):
    """
    display some user info to show we have authenticated successfully
    """
    print(request)
    twitter_user = 'katjamfitz'
    # twitter_user = request['twitter_user']
    api = get_api(request)
    timeline = api.user_timeline(twitter_user)
    # print(timeline)
    # print(timeline[0]._json)

    return render_to_response('timeline.html', {'timeline' : timeline})

def analyzed_timeline(request):
    """
    display some user info to show we have authenticated successfully
    """

    api = get_api(request)
    timeline = api.user_timeline('katjamfitz')
    # analyzed_timeline = botapi.analyze(timeline)
    # print(analyzed_timeline)

    return render_to_response('timeline.html', {'timeline' : timeline})
