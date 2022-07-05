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

## Playground 
Link of the pythonanywhere and explanation.


## Structure

<p align="center">
<img src="imgs/structure.png">
</p>


### 1- Data Source

If you have an account in Spotify, I´ll probably have heard of Genius. Genius is a website that allows users to provide annotations and interpretation to song lyrics, news stories, sources, poetry, and documents.

Spotify has had a partnership with Genius since 2016 on their "Behind the Lyrics" feature, which displays lyrics and content from Genius for select tracks, allowing users to "watch annotated lyrics for songs as you listen to them".

For this project we will use the [Genius.com API](https://genius.com/api-clients) to get the lyrics from the selected artist that we need to finetune the model. However, the very first milestone is to create an account into the developer site of Genius API, this will provide us with the access token or credentials required. Once we get to this point, let´s analyze what our code will do.


```python
    from flask import Flask,render_template, request
    # Using request to set the inputs coming from the html
    genius_access_token=request.form['GENIUS_ACCESS_TOKEN']
    # Set environment variables so the API will read this credentials
    os.environ['GENIUS_ACCESS_TOKEN'] = genius_access_token
```

In this first approach we will keep it simple but in the next version we will source [Spotify API](https://developer.spotify.com/dashboard/applications) so the user gains the feature of playing with the different parameters, such as the danceability, the energy and so on... that Spotify opens for exploration into their API.


### 2- Ingestion
Instead of calling directly the Data Source, which requires a good understanding of the Genius.com API documentation, we will take a more friendly approach by leveraging [Lyricsgenius](https://lyricsgenius.readthedocs.io/en/master/), a python wrapper for the Genius.com API that simplify the job.

First, the user will provide us through the
```python
    # Using request to set the inputs from the html
    input_lyrics=request.form['message']
    artist=request.form['ARTIST']
    max_songs=request.form['MAX_SONGS']
```



As mentioned before, in version2, this project will receive an upgrade by getting the information coming from Spotify, as we have already had a first hand experience with it on a previous Spark project, we can tell in advance that the intention is to facilitate the ingestion through  [Spotipy](https://spotipy.readthedocs.io/en/2.9.0/) a python wrapper for the Spotify API.

### 3- Storage


### 4- Processing
Why did we use GPT-2?

### 5- Serving


### 6- Visualization


### Sources
- [How to Fine-Tune GPT-2 for Text Generation](https://towardsdatascience.com/how-to-fine-tune-gpt-2-for-text-generation-ae2ea53bc272)
- [GPT-2 Artificial Intelligence Song Generator](https://blog.ml6.eu/gpt-2-artificial-intelligence-song-generator-lets-get-groovy-3e7c1f55030f)
- [How to Leverage Spotify API + Genius Lyrics for Data Science Tasks in Python](https://medium.com/swlh/how-to-leverage-spotify-api-genius-lyrics-for-data-science-tasks-in-python-c36cdfb55cf3)
- [Text Generation With Python And GPT-2](https://towardsdatascience.com/text-generation-with-python-and-gpt-2-1fecbff1635b)
- [Understanding the GPT-2 Source Code Part 1](https://medium.com/analytics-vidhya/understanding-the-gpt-2-source-code-part-1-4481328ee10b)
- [GPT2 fine tuning | gpt2 text generation | harry potter novel generation gpt2](https://www.youtube.com/watch?v=DNLebQ_vYiw&ab_channel=ProgrammingHut)
- [Deploying with Flask using Pythonanywhere](https://www.youtube.com/watch?v=5jbdkOlf4cY&ab_channel=PrettyPrinted)


### Who are we?
IE Students of the MSc Business Analytics & Big Data. Team Power Rangers:
  - Isobel Rae Impas
  - Jan P. Thoma
  - Nikolas Artadi
  - Camila Vasquez
  - Santiago Alfonso Galeano
  - Miguel Frutos

Made with ❤️ by Team Power Rangers
