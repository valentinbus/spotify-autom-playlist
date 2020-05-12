import requests
import os
import logging
import base64
import json

from app import db
from .models import (
    Category,
    CategoryTrack,
    Playlist,
    Track,
    TrackPlaylist,
    User
)

from pprint import pprint


logging.basicConfig(level=logging.DEBUG)
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET_ID')
API_TOKEN_URL = "https://accounts.spotify.com/api/token"

HOME_URL = os.getenv('HOME_URL')
URL = "https://accounts.spotify.com/authorize"
SCOPE_AUTHORIZATION = ['user-library-read', 'user-library-modify'] #see this url for more information ==> https://developer.spotify.com/documentation/general/guides/scopes/
REDIRECT_URL = os.getenv('REDIRECT_URL')

class Spotify:
    def __init__(self):
        self.baerer_token = None
        self.user_id = None


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


    def _get_user_id(self, token):
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
        user_id = result.json().get('id')
        
        #Create User if not exist
        if db.session.query(User).filter_by(id='valentinoiho').first() is None:
            u = User(id=user_id)
            db.session.add(u)
            db.session.commit()
            print('ok')

        self.user_id = user_id

        return user_id


    def get_tracks(self, token):
        """
        Get liked tracks from user
        """
        offset = 0

        headers = {
            'Authorization': token,
        }

        params = {
            'limit': 50,
            offset: offset
        }

        result = requests.get(
            url="https://api.spotify.com/v1/me/tracks",
            headers=headers,
            params=params
        )

        max_tracks = result.json().get('total')
        print(f"max result {max_tracks}")

        response = list()
        while offset <= max_tracks: #TODO we have to replace 50 per max_tracks
            print(offset)
            response.append(
                requests.get(
                    url="https://api.spotify.com/v1/me/tracks",
                    headers=headers,
                    params=params
                ).json()
            )
            offset+=50

        return response


    def _get_loved_track_id(self, token):
        """
        Get liked tracks from user
        """
        user_id = self._get_user_id(token)
        offset = 0

        headers = {
            'Authorization': token,
        }

        params = {
            'limit': 50,
            offset: offset
        }
        result = requests.get(
            url="https://api.spotify.com/v1/me/tracks",
            headers=headers,
            params=params
        )

        response = list()

        for item in result.json().get('items'):

            track = {
                'id': item.get('track').get('id'),
                'name': item.get('track').get('name'),
                'artist': item.get('track').get('artists')[0].get('id')
            }
            response.append(track)

            #Create tracks if not exist
            if db.session.query(Track).filter_by(id=track['id']).first() is None:
                t = Track(id=track['id'], name=track['name'], artist=track['artist'])
                db.session.add(t)
                db.session.commit()

        return response

    def _init_category(self, token):
        """
        Use to create and associate category with tracks
        """
        user_id = self.user_id

        


    def _init_first_playlist(self, token):
        """
        Use to create a playlist with all loved tracks to not call again spotify api
        """
        user_id = self._get_user_id(token)
        print(db.session.query(Playlist).filter_by(user_id=user_id, name="Loved Tracks").first())

        if db.session.query(Playlist).filter_by(user_id=user_id, name="Loved Tracks").first() is None:
            
            playlist = Playlist(name="Loved Tracks", user_id=user_id)
            db.session.add(playlist)
            db.session.commit()
            response =  {
                'message': "Good !",
                'playlist': {
                    'name': 'Loved Tracks',
                    'id': playlist.id
                }
            }

        else:
            playlist = db.session.query(Playlist).filter_by(user_id=user_id, name='Loved Tracks').first()

            #Create all connections to TrackPlaylist Table
            tracks = db.session.query(Track).all()
            for track in tracks:
                track_playlist = TrackPlaylist(playlist_id=playlist.id, track_id=track.id)


            response = {
                'message': "Good !",
                'playlist': {
                    'name': 'Loved Tracks',
                    'id': playlist.id
                }
            }
        return response

        
    # def _init_category(self, token):
    #     """
    #     Init Category
    #     """
    def get_artist_from_track(self, id_tracks, token):
        """
        Get artist from a track id
        """
        pass

