import requests
import json

# Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
token = 'BQC8e_Rd4fL8Ta-wiac6T48IvZOeHqjV-d6MXs-7FJKh-H3WhisfIEskskU7RO0FuCUCf56y5sg2LfCvhSxUQOWf3HW1LrA5Gkeyebq3qooYLDVGoPtXZSapVRQBkQB9-8sUWv2-HjHszgsgujkgTlHAm4tIjhfiOLMqAAML-zXmoIOT4lJgH0X-l2ZiPZJ1mfkrb5Rx_TzI1lgnRNlKaTod6dsA-iimPua7Q2IMb1slhNtBXHZaCyhmakd_bZpIsBXFx3STAOyk90jAR9Vv'

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

top_tracks = get_top_tracks()
for track in top_tracks:
    track_name = track['name']
    artists = ', '.join(artist['name'] for artist in track['artists'])
    print(f'{track_name} by {artists}')
