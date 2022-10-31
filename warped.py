from curses import meta
import requests
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import datetime
from pprint import pprint
import gspread


SPOTIPY_CLIENT_ID='463cf543d5524d528c212e926d5f7a7e'
SPOTIPY_CLIENT_SECRET='8ec9e99d9d5240c883e3782dc18aad5f'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
SCOPE = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=SCOPE)
)

top_tracks_short = sp.current_user_top_tracks(limit=10, offset=0, time_range="short_term")

def get_track_ids(time_frame):
    track_ids= []
    for song in time_frame['items']:
        track_ids.append(song['id'])
    return track_ids

track_ids = get_track_ids(top_tracks_short)

track_id = '4aM0fbIFtdDbwIrbioUHC0'

def get_track_features(id):
    meta = sp.track(id)
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    spotify_url = meta['external_urls']['spotify']
    album_cover = meta['album']['images'][0]['url']
    track_info = [name, album, artist, spotify_url, album_cover]
    return track_info

get_track_features(track_id)

#loop over tracks

tracks = []
for i in range(len(track_ids)):
    time.sleep(.5)
    track = get_track_features(track_ids[i])
    tracks.append(track)

pprint(tracks)

#creating the data set

df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'spotify_url', 'albun_cover'])
df.head(5)

gc = gspread.service_account(
    filename='/Users/marcramirez/Downloads/prefab-clover-243516-9270e4b7430d.json'
)

sh = gc.open("my-spotify-wrapped")
worksheet = sh.worksheet("short_term")
val = worksheet.acell('B5').value

#worksheet.update([df.columns.values.tolist()] + df.values.tolist())

#insert the tracks into the google sheet

def insert_to_gsheet(track_ids):
    #loop the track idea
    tracks = []
    for i in range(len(track_ids)):
        time.sleep(.5)
        track = get_track_features(track_ids[i])
        tracks.append(track)
    # create dataset
    df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'spotify_url', 'albun_cover'])
    #insert into google sheet
    gc = gspread.service_account(
    filename='/Users/marcramirez/Downloads/prefab-clover-243516-9270e4b7430d.json'
)
    sh = gc.open('my-spotify-wrapped')
    worksheet = sh.worksheet(f'{time_period}')
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    
time_ranges = ["short_term", "medium_term", "long_term"]
for time_period in time_ranges:
    top_tracks = sp.current_user_top_tracks(limit=20, offset=0, time_range=time_period)
    track_ids = get_track_ids(top_tracks)
    insert_to_gsheet(track_ids)

