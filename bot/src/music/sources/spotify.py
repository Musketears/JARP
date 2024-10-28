import requests
import base64

class SpotifyAPI:
    '''
    Auth and fetch Spotify playlist information, and generate song names to play through YouTube.
    '''
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_auth_token(self):
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_headers = {
            'Authorization': 'Basic ' + base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        }
        auth_body = {'grant_type': 'client_credentials'}
        response = requests.post(auth_url, headers=auth_headers, data=auth_body)
        return response.json()['access_token']

    def get_playlist_tracks(self, playlist_uri):
        token = self.get_auth_token()
        headers = {'Authorization': f'Bearer {token}'}
        url = f'https://api.spotify.com/v1/playlists/{playlist_uri}/tracks'
        params = {'fields': 'items(track(name,artists(name)))'}
        response = requests.get(url, headers=headers, params=params)
        items = response.json()['items']
        return [item['track'] for item in items]