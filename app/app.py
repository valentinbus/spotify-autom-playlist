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
        if session.get('baerer_token'):
            try:

                if isinstance(f().get_json(), list):
                    for element in f().get_json():
                        if element.get('error'):
                            return redirect('/authent')
                        else:
                            return f()

                elif f().get_json().get('error'):
                    return redirect('/authent')

                else:
                    return f()
            except AttributeError as e:
                logging.debug(f"ERROR:::::{e}")
                #return redirect('/authent')
        else:
            flash('You need to have a valid token')
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


# @api.route('/get-user')
# class ValidToken(Resource):
#     method_decorators = [valid_token] #call decorator valid_token
#     def get(self):
#         user_information = spotify._get_user(
#             session.get('baerer_token')
#         )
#         return Response(user_information)


@api.route('/get-tracks')
class GetTracks(Resource):
    method_decorators = [valid_token]
    def get(self):
        tracks = spotify.get_tracks(session.get('baerer_token'))
        return jsonify(tracks)

@api.route('/get-loved-track-id')
class GetTracks(Resource):
    method_decorators = [valid_token]
    def get(self):
        tracks = spotify._get_loved_track_id(session.get('baerer_token'))
        return jsonify(tracks)

@api.route('/init-first-playlist')
class GetTracks(Resource):
    method_decorators = [valid_token]
    def get(self):
        response = spotify._init_first_playlist(session.get('baerer_token'))
        return jsonify(response)


@app.route('/test', methods=["GET"])
def test():
    return render_template("test.html")


# @api.route('/get-cache', methods=["GET"])
# class GetCache(Resource):
#     method_decorators = [valid_token]
#     def get(self):
#         return get_tracks()


if __name__ == '__main__':
    app.run(
        debug=True,
        host=os.getenv('HOME_URL'),
    )
