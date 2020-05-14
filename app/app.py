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
from flask_restplus import Api, Resource
from functools import wraps

from pprint import pprint


logging.basicConfig(level=logging.DEBUG)
spotify = Spotify()

api = Api(app)

CORS(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

def valid_token(f):
    @wraps(f) #util if we use multiple times this decorator
    def wrap(*args, **kwargs):
        """
        TODO try with session.get('baerer') is valid with request...
        """
        if session.get('baerer_token') and session.get('baerer_token') != "Bearer None":
            logging.info("ICI:::In decorator")
            if isinstance(f().get_json(), list):
                for element in f().get_json():
                    if (
                        element.get('error').get('message') == "No token provided" or
                        element.get('error').get('message') == "Only valid bearer authentication supported" or
                        element.get('error').get('message') == "The access token expired"
                    ):
                        return redirect('/authent')        
            else:
                return f()
        else:
            logging.debug('You need to have a valid token')
            return redirect('/authent')
    return wrap


@api.route('/home')
class home(Resource):
    def get(self):
        return Response("Bienvenue")


@api.route('/authent')
class authent(Resource):
    def get(self):
        return redirect(spotify._authorization_ulr())


@api.route('/get-token')
class GetToken(Resource):
    def get(self):
        code = request.args.get('code')
        spotify._get_baerer_token(code)
        spotify._get_user_id(f'Bearer {spotify.baerer_token}')
        session['baerer_token'] = f'Bearer {spotify.baerer_token}'
        print(session)
        return Response('Vous êtes connecté')


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
        return jsonify(spotify.init_db(session.get('baerer_token')))


@api.route('/get-tracks')
class GetTracks(Resource):
    def get(self):
        """
        Get all tracks from authenticate user
        """
        return jsonify(spotify.get_tracks())


@api.route('/get-categories')
class GetCategories(Resource):
    def get(self):
        """
        Get all categories from authenticate user
        """
        return jsonify(spotify.get_categories())


@api.route('/get-user')
class GetUser(Resource):
    method_decorators = [valid_token]
    def get(self):
        return jsonify(spotify.get_user(session.get('baerer_token')))


@app.route('/test', methods=["GET"])
def test():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(
        debug=True,
        host=os.getenv('HOME_URL'),
    )
