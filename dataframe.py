from spotify_data import *


ids = []


# Loop through the results from spotify_data.py. Append the 'track' and 'id' to the ids list.
for item in results['tracks']['items']:
    track = item['track']['id']
    ids.append(track)


# Song data to be displayed.
song_meta = {'id':[], 'album':[], 'name':[], 'artist':[], 'explicit':[], 'popularity':[]}


for song_id in ids:
    meta = spot.track(song_id)

    # Append song id to the id list in the song meta dict.
    song_meta['id'].append(song_id)

    # Album name
    album = meta['album']['name']
    song_meta['album'].append(album)

    # Song name
    song = meta['name']
    song_meta['name'].append(song)

    # Artist's name. List comprehension to grab artist name and join on comma/space.
    s = ', '
    artist = s.join([singer_name['name'] for singer_name in meta['artists']])
    song_meta['artist'].append(artist)

    # Explicit
    explicit = meta['explicit']
    song_meta['explicit'].append(explicit)

    # Song popularity
    popularity = meta['popularity']
    song_meta['popularity'].append(popularity)


# Create dataframe from the song metadata using pandas.
song_meta_df = pd.DataFrame.from_dict(song_meta)

# Check the song feature
features = spot.audio_features(song_meta['id'])

# Change dictionary to dataframe.
features_df = pd.DataFrame.from_dict(features)

# Convert ms to min. Song duration currently in milliseconds.
features_df['duration_ms'] = features_df['duration_ms']/60000

final_df = song_meta_df.merge(features_df)

print(final_df)



