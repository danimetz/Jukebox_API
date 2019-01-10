from django.urls import path
from . import views

urlpatterns = [
    path('api/track/', views.TrackListCreate.as_view() ),
    # path('/search', views.search, name='')
    path('callback/', views.spotify_callback),
    path('', views.index),
    path('playlists/', views.playlists),
    path('search/', views.search),

]
