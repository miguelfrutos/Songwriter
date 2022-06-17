#!pip install lyricsgenius
#!pip install spotipy

import os
import time
import json
import spotipy
import lyricsgenius as lg
import configparser
import subprocess

import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

# Envionment Variables with ConfigParser
cfg = configparser.ConfigParser()
cfg.read('credentials.ini')

## Getting the environment variables from credentials.ini file
spotipy_client_id=cfg.get('CREDENTIALS','spotipy_client_id')
spotipy_client_secret=cfg.get('CREDENTIALS','spotipy_client_secret')
spotipy_redirect_uri=cfg.get('CREDENTIALS','spotipy_redirect_uri')
genius_access_token=cfg.get('CREDENTIALS','genius_access_token')

## Setting up the environment variables
os.environ.setdefault('SPOTIPY_CLIENT_ID', spotipy_client_id)
os.environ.setdefault('SPOTIPY_CLIENT_SECRET', spotipy_client_secret)
os.environ.setdefault('SPOTIPY_REDIRECT_URI', spotipy_redirect_uri)
os.environ.setdefault('GENIUS_ACCESS_TOKEN', genius_access_token)


######SPOTIFY API CONNECTION#########
# Spotify object with the Credentials

# ALTERNATIVELY: Set environment variables in Windows manually
### os.environ['SPOTIPY_CLIENT_ID'] = ''
### os.environ['SPOTIPY_CLIENT_SECRET'] = ''
### os.environ['GENIUS_ACCESS_TOKEN'] = ''

spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
spotify_secret = os.environ['SPOTIPY_CLIENT_SECRET']
#spotify_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
genius_access_token = os.environ['GENIUS_ACCESS_TOKEN']



#Spotify Credentials
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# Include the band or artist
artist_name = 'Queen'

# It will return the most popular artist first (sorted by popularity).
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



# List albums of an artist: example Birdy    
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
 

######GENIUS API CONNECTION#########    
#our genius_object
genius = lg.Genius(genius_access_token)

#search sequentially each song on Genius.com
for song_title in songs:
    single_song = genius.search_song(title=song_title,artist=artist_name)
    lyrics = single_song.lyrics
    print(lyrics)

#Print the songs searched
print(songs)


genius2 = lg.Genius('Client_Access_Token_Goes_Here', skip_non_songs=True, 
                   excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def get_lyrics(arr, k):
    c = 0
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:
            print(f"some exception at {name}: {c}")