from django.contrib import admin
from .models import Recentplayed, Song,Playlist,Favorite

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Favorite)
admin.site.register(Recentplayed)
# Register your models here.
