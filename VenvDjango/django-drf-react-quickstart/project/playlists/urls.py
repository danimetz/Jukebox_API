from django.urls import path
from . import views

urlpatterns = [
    path('playlist_save/', views.playlist_save ),
    # path('/search', views.search, name='')


]
