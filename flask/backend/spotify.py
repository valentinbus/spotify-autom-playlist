import requests
import os
import logging
import base64
import json

from pprint import pprint


logging.basicConfig(level=logging.DEBUG)
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET_ID')
API_TOKEN_URL = "https://accounts.spotify.com/api/token"

HOME_URL = "0.0.0.0/"
URL = "https://accounts.spotify.com/authorize"
SCOPE_AUTHORIZATION = ['user-library-read', 'user-library-modify' ] #see this url for more information ==> https://developer.spotify.com/documentation/general/guides/scopes/
REDIRECT_URL = "https://0.0.0.0:443/get-token"

class Spotify:
    def __init__(self):
        self.baerer_token = None

    def _authorization_ulr(self):
        """
        Give url for user authorization
        """
        data = {
            'redirect_uri': REDIRECT_URL,
            'client_id': CLIENT_ID,
            'response_type': 'code',
            'scope': SCOPE_AUTHORIZATION
        }
        r = requests.get(
            url=URL,
            params=data
        )
        return r.url

    def _get_baerer_token(self, code):
        """
        Get baerer token to authorize API calls
        """

        b64 = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode('UTF-8'))
        logging.info(f'Basic {b64}')

        headers = {
            'Authorization': f'Basic {b64.decode("UTF-8")}',
        }

        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URL
        }

        result = requests.post(
            url=API_TOKEN_URL,
            data=data,
            headers=headers
        )

        content = json.loads(result.content.decode('UTF-8'))
        self.baerer_token = content.get('access_token') #use for all api request
        return HOME_URL

    def get_user(self, token):
        """
        Get user information
        """
        headers = {
            'Authorization': token,
        }
        print(f"HEADERS:::{headers}")
        result = requests.get(
            url="https://api.spotify.com/v1/me/",
            headers=headers
        )

        return result.content
