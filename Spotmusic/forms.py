
from django.db import Form
from django import forms
from django.contrib.auth.forms import User


# Create your models here.
class Song(forms.Form):
    
    Language_Choice = (
        ('Spanish', 'Spanish'),
        ('English', 'English'),
        )

    name = forms.CharField(max_length=200)
    album = forms.CharField(max_length=200)
    language = forms.CharField(max_length=20,choices=Language_Choice,default='Spanish')
    song_img = forms.FileField()
    year = forms.IntegerField()
    singer = forms.CharField(max_length=200)
    song_file = forms.FileField()

    def __str__(self):
        return self.name


class Playlist(forms.Form):
    user = forms.ForeignKey(User, on_delete=forms.CASCADE)
    playlist_name = forms.CharField(max_length=200)
    song = forms.ForeignKey(Song, on_delete=forms.CASCADE)


class Favorite(forms.Form):
    id = forms.AutoField(primary_key=True)
    user = forms.ForeignKey(User, on_delete=forms.CASCADE)
    song = forms.ForeignKey(Song, on_delete=forms.CASCADE)
    is_fav = forms.BooleanField(default=False)


class Recentplayed(forms.Form):
    user = forms.ForeignKey(User, on_delete=forms.CASCADE)
    song = forms.ForeignKey(Song, on_delete=forms.CASCADE)
# Create your models here.
