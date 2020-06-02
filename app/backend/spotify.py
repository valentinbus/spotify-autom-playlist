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
REDIRECT_URL = os.getenv('REDIRECT_URL')
#REDIRECT_URL = "http://0.0.0.0:5000/get-token"
#see this url for more information ==> https://developer.spotify.com/documentation/general/guides/scopes/
SCOPE_AUTHORIZATION = (
    "user-read-private "
    "user-library-read "
    "user-library-modify "
    "playlist-modify-private "
    "playlist-modify-public"
)

class Spotify:
    def __init__(self):
        self.baerer_token = None
        self.user_id = None


    def _authorization_ulr(self):
        """
        Give url for user authorization
        """
        print(SCOPE_AUTHORIZATION)
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

    def _check_token(self, token):
        """
        Get user information
        """
        headers = {
            'Authorization': token,
        }

        result = requests.get(
            url="https://api.spotify.com/v1/me/",
            headers=headers
        )
        return result.json()

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
        display_name = result.json().get('display_name')
        photo = [photo.get('url') for photo in result.json().get('images')][0]

        #Create User if not exist
        if db.session.query(User).filter_by(id=user_id).first() is None and user_id is not None:
            u = User(id=user_id, photo=photo, display_name=display_name)
            db.session.add(u)
            db.session.commit()

        self.user_id = user_id

        return user_id


    def _init_loved_track(self, token, user_id):
        """
        Get liked tracks from user
        """

        offset = 0

        headers = {
            'Authorization': token,
        }

        params = {
            'limit': 50,
        }
        result = requests.get(
            url="https://api.spotify.com/v1/me/tracks",
            headers=headers,
            params=params
        )

        max_tracks = result.json().get('total')
        response = list()

        while offset <= max_tracks:
            params = {
                'limit': 50,
                offset: offset
            }
            result = requests.get(
                url="https://api.spotify.com/v1/me/tracks",
                headers=headers,
                params={
                    'limit': 50,
                    'offset': offset
                }
            )
            
            offset+=50

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


    def _init_category(self, token, user_id):
        """
        Use to create and associate category with tracks
        """

        headers = {
            'Authorization': token,
        }

        tracks = db.session.query(Track).all()
        genres = list()
        response = list()

        for track in tracks:
            result = requests.get(
            url=f"https://api.spotify.com/v1/artists/{track.artist}",
            headers=headers
            )

            if result.json().get('genres'):
                #print(result.json().get('genres'))
                for category_name in result.json().get('genres'):
                    if db.session.query(Category).filter_by(name=category_name).first() is None:
                        cat = Category(name=category_name)
                        db.session.add(cat)
                        db.session.commit()

                        category_id = db.session.query(Category).filter_by(name=category_name).first().id
                        track_id = track.id

                        response.append(
                            {
                                'category_id': category_id,
                                'category_name': category_name,
                            }
                        )



                    category_id = db.session.query(Category).filter_by(name=category_name).first().id
                    track_id = track.id
                    if db.session.query(CategoryTrack).filter_by(track_id=track_id).first() is None:
                        category_track = CategoryTrack(track_id=track_id, category_id=category_id)
                        db.session.add(category_track)
                        db.session.commit()

                    else:
                        category = db.session.query(Category).filter_by(name=category_name).first()
                        response.append(
                            {
                                'category_id': category.id,
                                'category_name': category.name
                            }
                        )

        return response


    def _init_first_playlist(self, token, user_id):
        """
        Use to create a playlist with all loved tracks to not call again spotify api
        """

        if db.session.query(Playlist).filter_by(user_id=user_id, name="Loved Tracks").first() is None:
            
            playlist = Playlist(name="Loved Tracks", user_id=user_id)
            db.session.add(playlist)
            db.session.commit()

            #Create all connections to TrackPlaylist Table
            tracks = db.session.query(Track).all()
            for track in tracks:
                if db.session.query(TrackPlaylist).filter_by(playlist_id=playlist.id, track_id=track.id).first() is None:
                    track_playlist = TrackPlaylist(playlist_id=playlist.id, track_id=track.id)
                    db.session.add(track_playlist)
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
                if db.session.query(TrackPlaylist).filter_by(playlist_id=playlist.id, track_id=track.id).first() is None:
                    track_playlist = TrackPlaylist(playlist_id=playlist.id, track_id=track.id)
                    db.session.add(track_playlist)
                    db.session.commit()


            response = {
                'message': "Good !",
                'playlist': {
                    'name': 'Loved Tracks',
                    'id': playlist.id
                }
            }
        return response


    def _add_track(self, token, playlist_name, playlist_id, user_id):
        """
        Add track to playlist
        """
        category_id = db.session.query(Category).filter_by(name=playlist_name).first().id
        playlist_id_db = db.session.query(Playlist).filter_by(name=playlist_name, user_id=user_id).first().id

        loved_track_playlist = db.session.query(Playlist).filter_by(user_id=user_id, name="Loved Tracks").first()
        user_loved_track = db.session.query(TrackPlaylist).filter_by(playlist_id=loved_track_playlist.id)
        list_track_id = list()

        for loved_track in user_loved_track:
            sql = f"SELECT track_id FROM \"category_track\" where category_id={category_id} and track_id='{loved_track.track_id}';"
            result = db.engine.execute(sql)
            result = [row[0] for row in result]
            # track_id = track_id[0]
            if result:
                track_id = result[0]
                if db.session.query(TrackPlaylist).filter_by(playlist_id=playlist_id_db, track_id=track_id).first() is None:
                    category_track = TrackPlaylist(playlist_id=playlist_id_db, track_id=track_id)
                    db.session.add(category_track)
                    db.session.commit()
                    
                    list_track_id.append(track_id)


        #Add tracks to spotify playlist
        i = 0
        while i <= len(list_track_id): #have to do this because if URI is too long request return 414
            headers = {
                'Authorization': token,
            }
            url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
            params = {
                'uris': ",".join([f"spotify:track:{element}" for element in list_track_id[i:i+50:]])
            }

            result = requests.post(
                headers=headers,
                params=params,
                url=url
            )

            i+=50

        return {'ok': 'super'}


    def init_db(self, token, user_id):
        """
        Call all actions to init db
        """
        #:
        if db.session.query(Playlist).filter_by(user_id=user_id, name="Loved Tracks").first() is None:
            self._get_user_id(token)
            self._init_loved_track(token, user_id)
            self._init_first_playlist(token, user_id)
            self._init_category(token, user_id)

            return {'message': 'Db is iniatilise with first Playlist Loved Tracks'}
    
        else:
            return {'message': 'Db already init'}


    def clear_db(self, token, user_id):
        """
        Clear db
        """
        playlists = Playlist.query.filter_by(user_id=user_id)
        [TrackPlaylist.query.filter_by(playlist_id=playlist.id).delete() for playlist in playlists]
        playlists.delete()
        User.query.filter_by(id=user_id).delete()
        db.session.commit()

        return {'message': 'Db is clear'}


    def get_tracks(self, user_id):
        """
        Get all loved tracks
        """
        response = list()
        playlist_id = db.session.query(Playlist).filter_by(user_id=user_id).first().id
        db.session.query(Track).filter_by(id=db.session.query(TrackPlaylist.track_id).filter_by(playlist_id=playlist_id))
        for track_id in db.session.query(TrackPlaylist.track_id).filter_by(playlist_id=playlist_id):
            track = Track.query.get(track_id)
            response.append(
                {
                    'id': track.id,
                    'name': track.name,
                    'artist': track.artist
                }
            )
        
        return response


    def get_categories(self, user_id):
        """
        Get all loved tracks
        """
        response = list()

        categories = db.session.query(Category).filter_by(user_id=user_id)
        for category in categories:
            response.append(
                {
                    'id': category.id,
                    'name': category.name
                }
            )

        return response


    def get_playlist(self, user_id):
        """
        Get Playlist based on Loved Tracks
        """
        response = list()

        playlists = db.session.query(Playlist).filter_by(user_id=user_id)

        for playlist in playlists:
            response.append(
                {
                    "playlist_name": playlist.name,
                    "playlist_id": playlist.id,
                    "spotify_id": playlist.spotify_id
                }
            )

        return response


    def get_user(self, user_id):
        """
        Call all actions to init db
        """

        response = list()

        user = User.query.get(user_id)

        return [{
            "user_id": user.id,
            "user_photo": user.photo
        }]
            

    def suggest_playlist(self, user_id):
        """
        Purpose category playlist based on categories that come up the most in the liked songs
        """
        response = {
            'relevant_category': list()
        }

        #Determine categories for a user based on loved tracks playlist
        playlist_id = db.session.query(Playlist).filter_by(user_id=user_id).first().id
        #print(f"PLAYLIST ID:::{playlist_id}")
        tracks_playlist = db.session.query(TrackPlaylist).filter_by(playlist_id=playlist_id)
        categories = list()
        for track_playlist in tracks_playlist:
            track_id = track_playlist.track_id
            try:
                category_id = db.session.query(CategoryTrack).filter_by(track_id=track_id).first().category_id
                categories.append(category_id)
            except AttributeError:
                #print('Track has no category')
                pass

        #print(f"CATEGORIES:::{categories}")
        #Get top 10 category most recurent
        category_counter = {}
        for category in categories:
            if category in category_counter:
                category_counter[category] += 1
            else:
                category_counter[category] = 1

        revelant_cat = sorted(category_counter, key = category_counter.get, reverse = True)
        top_10 = revelant_cat[:10]
        #print(top_10)

        for category_id in top_10:
            query = db.session.query(Category).filter_by(id=category_id).first()
            d = {
                "name": query.name,
                "id": query.id
            }
            response['relevant_category'].append(d)

        return response


    def create_playlist(self, q, token, user_id):
        """
        Create playlist for user request
        """
        if q.isdigit() and db.session.query(Category).filter_by(id=q).first() is not None:
            playlist_name = db.session.query(Category).filter_by(id=q).first().name

            #Check if playlist already exist for user
            sql = f"SELECT * FROM \"playlist\" WHERE name='{playlist_name}' and user_id='{user_id}';"
            result = db.engine.execute(sql)
            result = [row[0] for row in result]

            pprint(f"RESULT:::{result}")


            if not result: #if playlist does not exist
                headers = {
                    'Authorization': token,
                }

                data = {
                    "name": playlist_name,
                    "description": f"Your favorite {playlist_name} tracks",
                    "public": False
                }

                result = requests.post(
                    url=f"https://api.spotify.com/v1/users/{user_id}/playlists",
                    headers=headers,
                    data=json.dumps(data)
                )

                if db.session.query(Playlist).filter_by(name=playlist_name, user_id=user_id).first() is None:
                    playlist = Playlist(name=playlist_name, user_id=user_id, spotify_id=result.json().get('id'))
                    db.session.add(playlist)
                    db.session.commit()

                self._add_track(token, playlist_name, result.json().get('id'), user_id)
                #return result.json()
                return {
                    "message": "playlist is create",
                    "playlist_name": playlist_name,
                    "playlist_id": result.json().get('id')
                }

            else:
                return {
                    "message": "playlist already exists"
                }
        else:
            return {
                "message": "You have to choose an existing category"
            }


#TODO add all delete and update/sync methods






    # def _check_existing_playlist(self, token, playlist_name):
    #     """
    #     Check if a playlist exist on spotify account
    #     TODO it works but I think there is a delay between playlist creation
    #     and when it appears on spotify so does not well
    #     """
    #     headers = {
    #         'Authorization': token,
    #     }

    #     params = {
    #         'limit': 50
    #     }

    #     url = "https://api.spotify.com/v1/me/playlists"

    #     result = requests.get(
    #         headers=headers,
    #         url=url
    #     )

    #     pprint(result.json())
    #     for item in result.json().get('items'):
    #         #If playlist exists return false
    #         if item.get('name') == playlist_name:
    #             return {
    #                 "response": False,
    #                 "playlist_name": playlist_name,
    #                 "playlist_id": item.get('id')
    #             }
    #     #TODO Ce n'est pas ordonné il faut donc que je retourne la bonne valeur, ici je retourne toujours la même playlist
    #     return {
    #         "response": True,
    #         "playlist_name": playlist_name,
    #         "playlist_id": "Does not exist yet"
    #     }