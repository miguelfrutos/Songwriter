# My Muppet is a Songwriter 
<p align="center">
<img width="350" height="200" src="imgs/ed.gif">
</p>

# Project Motivation
The music industry and artists are under pressure to generate higher output more quickly. Harnessing creativity and overcoming writers’ blocks when writing lyrics and music pieces are challenging.

# Solution
Helping artists create song texts more efficiently.

### Assignment Description
Our Natural Language Processing professor, Angel Castellanos Gonzalez, has proposed us a challenge. Create an application that should address an actual use case scenario, we came up with 

and you must justify your work: why and where is it
needed? Is there any other approach/system trying to solve this use case? What is your system
offering, not offered by other systems? In a word, you have to sell me your product in a way that I
buy it.
This must be a practical exercise; you have to implement something that actually works. I am aware
that you cannot program Alexa in 3 weeks, but you should offer something that actually works. It
can be a demo or a POC showing the functionalities of the actual system. You should propose the
rest of the functionalities of your system as future work but based on the features that you have
implemented.
You can use any of the tools explained in class and other resources available.
You should carry out a short review of the field in which the system applies.

 To deploy an end-to-end real-time solution following the next stages throughout the pipeline:<br>
  1- Select the **Data Source**: Twitter API.<br>
  2- **Ingestion**: Producer - Python app.<br>
  3- **Stream Storage**: Broker - Kafka.<br>
  4- **Processing**: Consumer - Spark Streaming.<br>
  5- **Serving**: Relational DB - MariaDB.<br>
  6- **Visualization**: Superset.<br>
![pipeline](Imgs/pipeline_snapshot.png)
### Who are we?
IE Students of the MSc Business Analytics & Big Data. Team Power Rangers:
  - Isobel Rae Impas
  - Jan P. Thoma
  - Nikolas Artadi
  - Camila Vasquez
  - Santiago Alfonso Galeano
  - Miguel Frutos

# Ukraine_tweets
### 1- Select the Data Source: Twitter API
Setting up Spotify. You need to create a "Spotify App". Follow the next steps:
- Visit [Projects & Apps](https://developer.spotify.com/dashboard/applications) section in the Developer Portal
- Sign into your Spotify account. (if you don't have one you should create it).
- Click the “Create an app” button.
- Fill-in the form (at least the required fields).
- Grab the details to setup the ingestion script later on.
- If all goes well, your Twitter App should be created and the API Key, API Secret Key will show up.
- The Access Token and Access Token Secret will be also needed.

Fill up the **credentials.ini** file with the required fields.

### 2- Ingestion - Producer (Python app)
[Tweepy](http://www.tweepy.org/)  is a python wrapper for the Twitter API that allowed us to easily collect tweets in real-time.
