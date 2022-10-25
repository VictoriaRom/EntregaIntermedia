from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('home', views.index, name='index'),
    path('<int:song_id>/', views.detail, name='detail'),
    path('mysongs/', views.mysongs, name='mysongs'),
    path('playlist/', views.playlist, name='playlist'),
    path('playlistsongs/<str:playlist_name>/', views.playlistsongs, name='playlistsongs'),
    path('favorite/', views.favorite, name='favorite'),
    path('allsongs/', views.allsongs, name='allsongs'),
    path('recentplayed/', views.recentplayed, name='recentplayed'),
    path('spanishsongs/', views.spanishsongs, name='spanishsongs'),
    path('englishsongs/', views.englishsongs, name='englishsongs'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),
    path('play_song/<int:song_id>/', views.play_song_index, name='play_song_index'),
    path('play_recent_song/<int:song_id>/', views.play_recent_song, name='play_recent_song'),

]
