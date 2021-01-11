import spotipy
import pandas as pd
import json
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "f607746d600d4ce9ac4089a44c832475"
client_secret = "f94376c20039457e90d5d18b874d0955"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spot = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = "spotify:playlist:37i9dQZF1EMdY30Sxip47Z"

results = spot.playlist(playlist_id)