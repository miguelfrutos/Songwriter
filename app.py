# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:56:27 2022

@author: jpthoma and miguelfrutos
"""
#pip install gpt_2_simple
import gpt_2_simple as gpt2
import configparser
from flask import Flask,render_template, request
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

app = Flask(__name__,template_folder="templates")

@app.route("/")
#@app.route("/home")
def home():
    return render_template("index.html")


#Set a post method to yield predictions on page
@app.route('/', methods = ['POST'])
def predict():
    # Using request to set the inputs from the html
    genius_access_token=request.form['GENIUS_ACCESS_TOKEN']
    input_lyrics=request.form['message']
    artist=request.form['ARTIST']
    max_songs=request.form['MAX_SONGS']

    # Set environment variables
    os.environ['GENIUS_ACCESS_TOKEN'] = genius_access_token

    # Convert strings into list 
    artists = (Convert(artist))
    max_songs = int(max_songs)

    #our genius_object
    genius = lg.Genius(genius_access_token,
                        skip_non_songs=True,
                        excluded_terms=["Remix", "Live","Demo", "(Remix)", "(Live)"],
                        remove_section_headers=True)

    # Set up the file to write lyrics to (.txt) and erease previous content
    file = open('train_dataset.txt', 'r+')
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
    with open('train_dataset.txt', 'r+') as file:
        text = file.read()
    # Delete text and Write
    with open('train_dataset.txt', 'w') as file:
        # Delete
        new_text = re.sub('\d{2}Embed', '',text)
        # Write
        file.write(new_text)

    # Download the small version of GPT2
    gpt2.download_gpt2(model_name='124M')

    # Prepare the train_set
    file_name = 'train_dataset.txt'

    ## Finetune the model

    #model_name: model downloded
    #steps: number of epocs
    #sample_every: Number of steps to print example output
    #print_every: Number of steps to print training progress
    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess,
                dataset=file_name,
                model_name='124M',
                steps=20,
                restore_from='fresh',
                run_name='run1',
                print_every=10,
                sample_every=20,
                )


    ## Run_test with some parameters

    #lenght: number of tokes to generate
    #temperature: randomness in the value
    #prefix: start from this particular sentence
    #top_k: Number of words considered at each step(token).
    output= gpt2.generate(sess,
                length=250,
                temperature=0.7,
                prefix=input_lyrics,
                nsamples=5,
                top_k=40,
                return_as_list=True)
    #Converting list into a string
    output_string = ''.join(output)
    #rendering the output in the index.html file
    return render_template('index.html', prediction_text=output_string)


if __name__=="__main__":
    app.run(debug=True)
