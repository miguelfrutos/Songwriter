# My Muppet is a Songwriter 
<p align="center">
<img width="350" height="200" src="imgs/ed.gif">
</p>

## Project Motivation
Our Natural Language Processing professor, Angel Castellanos Gonzalez, has proposed us a challenge. Create an application that should address an actual use case scenario. Some people in our group play instruments and we have even tried to write songs, with unfortunate results, specially to our audience (family and friends) that were expecting a new Lady Gaga and Freddie Mercury in the room and after few songs realizing that maybe we should think of doing something else. Should we abandon our dreams?.

## Solution
A novel musician, real artists and the entire music industry are under pressure to generate higher output more quickly. Harnessing creativity and overcoming songwriters’ blocks when writing lyrics and music pieces are challenging. Our solution is helping artists create song texts more efficiently.

## Abstract
Natural Language Generation (NLG) has made incredible strides in recent years. In early 2019, OpenAI released GPT-2, a huge pretrained model (1.5B parameters) capable of generating text of human-like quality.

Generative Pretrained Transformer 2 (GPT-2) is, like the name says, based on the Transformer. It therefore uses the attention mechanism, which means it learns to focus on previous words that are most relevant to the context in order to predict the next word (for more on this, go here).

The goal of this repo is to show you how you can fine-tune GPT-2 to generate lyrics, based on the data you provide to it and the inputs. The idea is then to use the already trained GPT-2  model, fine-tune it to our specific data and then, based on what the model observes, generate what should follow in any given song.


## Structure

<p align="center">
<img src="imgs/structure.png">
</p>



### 1- Ingestion
- [Spotipy](https://spotipy.readthedocs.io/en/2.9.0/) is a python wrapper for the Spotify API.
- [Lyricsgenius](https://lyricsgenius.readthedocs.io/en/master/) is a python wrapper for the Genius.com API.
- [Spotify API](https://developer.spotify.com/dashboard/applications) 
- [Genius.com API](https://genius.com/api-clients)
In this first approach we will 



### Who are we?
IE Students of the MSc Business Analytics & Big Data. Team Power Rangers:
  - Isobel Rae Impas
  - Jan P. Thoma
  - Nikolas Artadi
  - Camila Vasquez
  - Santiago Alfonso Galeano
  - Miguel Frutos

Made with ❤️ by Team Power Rangers
