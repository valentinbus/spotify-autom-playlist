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
    flash,
    render_template
)
from backend.spotify import Spotify
from flask_cors import CORS
from flask_caching import Cache
from flask_restplus import Api, Resource
from functools import wraps

from pprint import pprint


logging.basicConfig(level=logging.DEBUG)
spotify = Spotify()

app = Flask(__name__)
api = Api(app)

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
        session['baerer_token'] = f'Bearer {spotify.baerer_token}'
        return Response('Vous êtes connecté')


@api.route('/get-user')
class ValidToken(Resource):
    method_decorators = [valid_token]
    def get(self):
        user_information = spotify.get_user(
            session.get('baerer_token')
        )
        return jsonify(user_information)


@api.route('/get-tracks')
class GetTracks(Resource):
    method_decorators = [valid_token]
    def get(self):
        tracks = spotify.get_tracks(session.get('baerer_token'))
        return jsonify(tracks)

@app.route('/test', methods=["GET"])
def test():
    return render_template("test.html")


@api.route('/get-cache', methods=["GET"])
class GetCache(Resource):
    method_decorators = [valid_token]
    def get(self):
        return get_tracks()


if __name__ == '__main__':
    app.run(
        debug=True,
        host=os.getenv('HOME_URL'),
    )
