import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Spotify token from environment variable
token = os.getenv('SPOTIFY_TOKEN')

def fetch_web_api(endpoint, method='GET', body=None):
    url = f'https://api.spotify.com/{endpoint}'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    if method == 'GET':
        response = requests.get(url, headers=headers)
    else:
        response = requests.request(method, url, headers=headers, data=json.dumps(body))
    return response.json()

def get_top_tracks():
    # Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    endpoint = 'v1/me/top/tracks?time_range=long_term&limit=5'
    return fetch_web_api(endpoint)['items']

def get_recommendations(top_tracks_ids):
    # Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-recommendations
    endpoint = f'v1/recommendations?limit=5&seed_tracks={",".join(top_tracks_ids)}'
    return fetch_web_api(endpoint)['tracks']

# Get top tracks
top_tracks = get_top_tracks()
for track in top_tracks:
    track_name = track['name']
    artists = ', '.join(artist['name'] for artist in track['artists'])
    print(f'{track_name} by {artists}')

# Top track IDs
top_tracks_ids = [
    '5I8wqCZfqMXhJ8NYwFHgwc', '4hAUynwghvrqDXs1ejKNEq', '07g3QpOdaG7kMQUqreh6vn',
    '62p6cgUc0cdguS1DttbfKU', '0WtM2NBVQNNJLh6scP13H8'
]

# Get recommendations based on top track IDs
recommended_tracks = get_recommendations(top_tracks_ids)
for track in recommended_tracks:
    track_name = track['name']
    artists = ', '.join(artist['name'] for artist in track['artists'])
    print(f'Recommended: {track_name} by {artists}')
