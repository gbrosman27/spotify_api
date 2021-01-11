from spotify_data import results

ids = []

for item in results['tracks']['items']:
    track = item['track']['id']
    ids.append(track)