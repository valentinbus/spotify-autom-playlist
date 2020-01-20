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


class Spotify:
    def __init__(self):
        self.baerer_token = None

    def _get_baerer_token(self):
        """
        Get baerer token to authorize API calls
        """

        b64 = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode('UTF-8'))
        logging.info(f'Basic {b64}')

        headers = {
            'Authorization': f'Basic {b64.decode("UTF-8")}',
        }

        data = {
            'grant_type': 'client_credentials'
        }

        result = requests.post(
            url=API_TOKEN_URL,
            data=data,
            headers=headers
        )

        content = json.loads(result.content.decode('UTF-8'))
        self.baerer_token = content.get('access_token')


    def _get_user_id(self):
        """
        Get id from name
        """

        pass


spotify = Spotify()
spotify._get_baerer_token()