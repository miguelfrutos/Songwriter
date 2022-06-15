#!pip install lyricsgenius
#!pip install spotipy

import os
import time
import json
import spotipy
import lyricsgenius as lg

import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

#Envionment Variables

## Include in the environment the following temporal variables

### export SPOTIPY_CLIENT_ID=''
### export SPOTIPY_CLIENT_SECRET=''
### export SPOTIPY_REDIRECT_URI=''
### export GENIUS_ACCESS_TOKEN=''

spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
spotify_secret = os.environ['SPOTIPY_CLIENT_SECRET']
spotify_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
genius_access_token = os.environ['GENIUS_ACCESS_TOKEN']

#Spotify Credentials
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

#Include the band or artist
artist_name = 'Queen'

#it will return the most popular artist first (sorted by popularity).
results = spotify.search(q='artist:' + artist_name, type='artist')
items = results['artists']['items']

#get the first result
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['uri'])

# uri as the ID of the artist
uri = artist['uri']

# we have the uri, now we need 10 songs of the artist
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(uri)

#including the songs into a list
songs = []
for track in results['tracks'][:10]:
    songs.append(track['name'])

#our genius_object
genius = lg.Genius(genius_access_token)

#search sequentially each song on Genius.com
for song_title in songs:
    single_song = genius.search_song(title=song_title,artist=artist_name)
    lyrics = single_song.lyrics
    print(lyrics)

#Print the songs searched
print(songs)
