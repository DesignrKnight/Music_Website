# Music_Website
A music streaming platform
Song API using Python Flask, SQL Alchemy and Marshmallow 

## Start With Pipenv

```python

# Activate virtual Environment 
$ pipenv shell
(or create a virtual env)
# Install dependencies
$ pipenv install

# Run Server (http://localhst:5000)
python app.py

```

## Functions
A user can upload/download/play/search songs.
All songs go into a common playlist.

## API Call
Local Host

http://127.0.0.1:5000

Upload a song

http://127.0.0.1:5000/uploadMusic 

View Playlist(JSON format)

http://127.0.0.1:5000/product

Unique URL to each song ID

http://127.0.0.1:5000/product/id

Search a song

http://127.0.0.1:5000/search

