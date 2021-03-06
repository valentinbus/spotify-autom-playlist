"""
To authent user have to go on /authent
"""
import json
import logging
import os
from app import app
from flask import (
    Flask,
    request,
    jsonify,
    Response,
    redirect,
    session,
    flash,
    render_template
)
from .backend.models import (
    User, 
    Playlist
)
from .backend.spotify import Spotify
from flask_cors import CORS
from flask_caching import Cache
from flask_restplus import Api, Resource, cors
from functools import wraps

from pprint import pprint


logging.basicConfig(level=logging.DEBUG)
spotify = Spotify()

CORS(app)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

"""
|---------------------------------|
| HERE ALL ROUTES FOR API PROCESS |                                
|---------------------------------|
"""

def valid_token(f):
    @wraps(f) #util if we use multiple times this decorator
    def wrap(*args, **kwargs):
        """
        TODO try with session.get('baerer') is valid with request...
        """
        res = f()
        if session.get('baerer_token') and session.get('baerer_token') != "Bearer None":
            logging.info("In decorator")
            if isinstance(res.get_json(), list):
                for element in res.get_json():
                    if (
                        element.get('error').get('message') == "No token provided" or
                        element.get('error').get('message') == "Only valid bearer authentication supported" or
                        element.get('error').get('message') == "The access token expired"
                    ):
                        return redirect('/authent') #attach get paramater to redirect
            else:
                return res
        elif session.get('baerer_token') is None:
            logging.debug('You need to have a valid token')
            return redirect('/authent')
    return wrap


@api.route('/authent')
class authent(Resource):
    def get(self):
        #return redirect(spotify._authorization_ulr())
        return jsonify(spotify._authorization_ulr())


@api.route('/get-token')
class GetToken(Resource):
    def get(self):
        code = request.args.get('code')
        print(f'code:::{code}')
        spotify._get_baerer_token(code)
        user_id = spotify._get_user_id(f'Bearer {spotify.baerer_token}')
        baerer_token = f'Bearer {spotify.baerer_token}'
        session['baerer_token'] = baerer_token
        session['user_id'] = user_id
        logging.info(session)
        return { 
            'user_id': user_id,
            'baerer_token': baerer_token
        }

        # return {
        #     'jwt': jwt_token #dans lequel je peux mettre le user id et le baerer token
        # }


@api.route('/init-db')
class InitDb(Resource):
    method_decorators = [valid_token]
    def get(self):
        """
        Call different method to init DB
        All loved tracks from authenticate user
        Init 'Loved Tracks' Playlist with all loved tracks to improve speed for next actions
        Init all categories based on tracks. Only solution was to get categories from artist
        because Spotify API do not give genres by tracks
        Init all relation table
        """
        #print(spotify.init_db(session.get('baerer_token')))
        #return jsonify(spotify.init_db(session.get('baerer_token')))
        return jsonify(spotify.init_db(session.get('baerer_token')))

    def put(self):
        """
        Call different method to init DB
        All loved tracks from authenticate user
        Init 'Loved Tracks' Playlist with all loved tracks to improve speed for next actions
        Init all categories based on tracks. Only solution was to get categories from artist
        because Spotify API do not give genres by tracks
        Init all relation table
        """
        #print(spotify.init_db(session.get('baerer_token')))
        #return jsonify(spotify.init_db(session.get('baerer_token')))
        return jsonify(spotify.init_db(session.get('baerer_token')))


@api.route('/get-tracks')
class GetTracks(Resource):
    def get(self):
        """
        Get all tracks from authenticate user
        """
        return jsonify(spotify.get_tracks(session['user_id']))


@api.route('/get-categories')
class GetCategories(Resource):
    def get(self):
        """
        Get all categories from authenticate user
        """
        return jsonify(spotify.get_categories(session['user_id']))


@api.route('/get-playlist')
class GetCategories(Resource):
    def get(self):
        """
        Get all playlist from authenticate user
        """
        return jsonify(spotify.get_playlist(session['user_id']))


@api.route('/get-user')
class GetUser(Resource):
    def get(self):
        """
        Get basic user informations
        """
        print(f"HEADER:::{request.headers}")
        #user_id = request.args.get('user_id')
        #return jsonify(spotify.get_user(user_id))
        return jsonify(spotify.get_user("valentinoiho"))


@api.route('/get-suggest-playlist')
class GetSuggestPlaylist(Resource):
    def get(self):
        return jsonify(spotify.suggest_playlist())


@api.route('/create-playlist')
@api.doc(body={'category_id': 'A category ID'})
class CreatePlaylist(Resource):
    method_decorators = [valid_token]
    def post(self):
        """
        Create Playlist from user request form
        """
        q = request.form['category_id']

        if q:
            return jsonify(spotify.create_playlist(q, session.get('baerer_token')))
        else:
            return jsonify({
                "message": "No category chosen"
            })

    def get(self):
        """
        Create Playlist from user request form
        """
        q = request.args.get("q")
        return jsonify(spotify.create_playlist(q, session.get('baerer_token')))



"""
|---------------------------------|
|           HERE MAIN             |                                
|---------------------------------|
"""
if __name__ == '__main__':
    app.run(
        debug=True,
        host=os.getenv('HOME_URL'),
    )
