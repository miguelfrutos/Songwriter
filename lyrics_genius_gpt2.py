#!pip install lyricsgenius
#!pip install spotipy

import os
import time
import json
import spotipy
import lyricsgenius as lg
import configparser
import subprocess
import re
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

def Convert(string):
    'Python function to convert string to list'
    li = list(string.split(","))
    return li

# Envionment Variables with ConfigParser
cfg = configparser.ConfigParser()
cfg.read('user.ini')

## Getting the environment variables from users.ini file
genius_access_token=cfg.get('CREDENTIALS','genius_access_token')

# Getting the path of the txt file, the name of the artists and the max_songs
path_txt=cfg.get('TRAIN_DATASET','path_txt')
artist=cfg.get('INPUTS','artist')
max_songs=cfg.get('INPUTS','max_songs')

# Convert strings into list 
artists = (Convert(artist))
max_songs = int(max_songs)

#our genius_object
genius = lg.Genius(genius_access_token,
                    skip_non_songs=True,
                    excluded_terms=["Remix", "Live","Demo", "(Remix)", "(Live)"],
                    remove_section_headers=True)

# Set up the file to write lyrics to (.txt) and erease previous content
file = open(path_txt, 'r+')
file.truncate(0)

def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in arr
    c = 0  # Counter
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n  \n \n".join(s))
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:  #  Broad catch which will give us the name of artist and song that threw the exception
            print(f"some exception at {name}: {c}")



#Specify the artists
get_lyrics(artists, max_songs)

# Some Cleaning
# Read file.txt
with open(path_txt, 'r+') as file:
    text = file.read()
# Delete text and Write
with open(path_txt, 'w') as file:
    # Delete
    new_text = re.sub('\d{2}Embed', '',text)
    # Write
    file.write(new_text)
