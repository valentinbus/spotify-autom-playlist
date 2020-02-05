"""
To authent user have to go on /authent
"""
import json
import logging
import os
from flask import (
    Flask,
    request,
    jsonify,
    Response,
    redirect,
    session,
    flash
)
from backend.spotify import Spotify
from flask_cors import CORS
from flask_caching import Cache
from functools import wraps

from pprint import pprint


logging.basicConfig(level=logging.DEBUG)
spotify = Spotify()

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "secret_keyoidozinfoinoqifnoeinosifn"
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

            except Exception as e:
                logging.debug(f"EROR::::: {e}")
        else:
            flash('You need to have a valid token')
            return redirect('/authent')
    return wrap

@app.route('/', methods=["GET"])
def home():
    return Response("Bienvenue")


@app.route('/authent', methods=["GET"])
def authent():
    return redirect(spotify._authorization_ulr())


@app.route('/get-token', methods=["GET"])
def get_token():
    code = request.args.get('code')
    spotify._get_baerer_token(code)
    session['baerer_token'] = f'Bearer {spotify.baerer_token}'
    return Response('Vous êtes connecté :)')


@app.route('/get-user', methods=["GET"])
@valid_token
def get_user():
    user_information = spotify.get_user(
        session.get('baerer_token')
    )
    return jsonify(user_information)


@app.route('/get-tracks', methods=["GET"])
@cache.cached(timeout=1000)
@valid_token
def get_tracks():
    tracks = spotify.get_tracks(session.get('baerer_token'))
    return jsonify(tracks)


@app.route('/get-cache', methods=["GET"])
@cache.cached(timeout=1000)
@valid_token
def get_cache():
    return get_tracks()


if __name__ == '__main__':
    app.run(
        debug=True,
        host=os.getenv('HOME_URL'),
    )
