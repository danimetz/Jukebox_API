from django.urls import path
from . import views

urlpatterns = [
    path('playlist_save/', views.playlist_save ),
    path('add_track/', views.add_track)
    # path('/search', views.search, name='')


]
