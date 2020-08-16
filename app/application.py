"""
To authent user have to go on /authent
"""
import json
import logging
import os
from app import application
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
import jwt

from pprint import pprint


logging.basicConfig(level=logging.DEBUG)
spotify = Spotify()

CORS(application)
api = Api(application)
application.config['CORS_HEADERS'] = 'Content-Type'

cache = Cache(application, config={'CACHE_TYPE': 'simple'})

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
        try:
            if isinstance(res.get_json(), list):
                for element in res.get_json():
                    if (
                        element.get('error').get('message') == "No token provided" or
                        element.get('error').get('message') == "Only valid bearer authentication supported" or
                        element.get('error').get('message') == "The access token expired"
                    ):
                        return {"error": "Baerer token is not valid"} #attach get paramater to redirect
        except:
            pass
        return res
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
        jwt_token = jwt.encode(
            {
                'user_id': user_id,
                'baerer_token': baerer_token
            },
            os.getenv('SECRET_KEY'),
            algorithm='HS256'
        )

        return {"jwt_token": jwt_token.decode('UTF-8')}


@api.route('/check-token')
class CheckToken(Resource):
    def get(self):
        try:
            jwt_token = request.headers.get('jwt_token')
            baerer_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('baerer_token')
            #baerer_token = "test expired token"
            return spotify._check_token(baerer_token)
        except jwt.exceptions.DecodeError as e:
            return {"error": f"{e}:::Check Jwt token"}

        return {"message": "Jwt token is valid"}


@api.route('/init-db')
class InitDb(Resource):
    def put(self):
        """
        Call different method to init DB
        All loved tracks from authenticate user
        Init 'Loved Tracks' Playlist with all loved tracks to improve speed for next actions
        Init all categories based on tracks. Only solution was to get categories from artist
        because Spotify API do not give genres by tracks
        Init all relation table
        """
        jwt_token = request.headers.get('jwt_token')
        baerer_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('baerer_token')
        user_id = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('user_id')

        return jsonify(spotify.init_db(baerer_token, user_id))


@api.route('/clear-db')
class ClearDb(Resource):
    def delete(self):
        """
        Clear DB
        """
        jwt_token = request.headers.get('jwt_token')
        baerer_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('baerer_token')
        user_id = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('user_id')

        return jsonify(spotify.clear_db(baerer_token, user_id))

@api.route('/get-tracks')
class GetTracks(Resource):
    def get(self):
        """
        Get all tracks from authenticate user
        """
        jwt_token = request.headers.get('jwt_token')
        user_id = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('user_id')
        return jsonify(spotify.get_tracks(user_id))


@api.route('/get-categories')
class GetCategories(Resource):
    def get(self):
        """
        Get all categories from authenticate user
        """
        jwt_token = request.headers.get('jwt_token')
        user_id = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('user_id')
        return jsonify(spotify.get_categories(user_id))


@api.route('/get-playlist')
class GetCategories(Resource):
    def get(self):
        """
        Get all playlist from authenticate user
        """
        jwt_token = request.headers.get('jwt_token')
        user_id = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('user_id')
        return jsonify(spotify.get_playlist(user_id))


@api.route('/get-user')
class GetUser(Resource):
    def get(self):
        """
        Get basic user informations
        """
        jwt_token = request.headers.get('jwt_token')
        user_id = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('user_id')
        print(f"user id :::{user_id}")
        return jsonify(spotify.get_user(user_id))


@api.route('/get-suggest-playlist')
class GetSuggestPlaylist(Resource):
    def get(self):
        jwt_token = request.headers.get('jwt_token')
        user_id = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('user_id')
        return jsonify(spotify.suggest_playlist(user_id))


@api.route('/create-playlist')
@api.doc(body={'category_id': 'A category ID'})
class CreatePlaylist(Resource):
    def post(self):
        """
        Create Playlist from user request form
        """
        q = request.form['category_id']
        jwt_token = request.headers.get('jwt_token')
        baerer_token = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('baerer_token')
        user_id = jwt.decode(jwt_token, os.getenv('SECRET_KEY'), algorithm="HS256").get('user_id')

        if q:
            return jsonify(spotify.create_playlist(q, baerer_token, user_id))
        else:
            return jsonify({
                "message": "No category chosen"
            })



"""
|---------------------------------|
|           HERE MAIN             |                                
|---------------------------------|
"""
if __name__ == '__main__':
    application.run(
        debug=True,
        host='164.90.234.101',
        port=5000
    )
