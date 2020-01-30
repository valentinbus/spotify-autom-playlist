"""
To authent user have to go on /authent
"""
import json
from flask import (
    Flask,
    request,
    render_template,
    jsonify,
    Response,
    redirect,
    session,
    flash
)
from flask_session import Session
from backend.spotify import Spotify
from flask_cors import CORS, cross_origin

from pprint import pprint



spotify = Spotify()

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "secret_keyoidozinfoinoqifnoeinosifn"

def valid_token(f):
    def wrap():
        if session.get('baerer_token'):
            return f()
        else:
            flash('You need to have a valid token')
            return redirect('/authent')
    return wrap

@app.route('/', methods=["GET"])
def home():
    return Response("Vous êtes authentifié :)")


@app.route('/authent', methods=["GET"])
def authent():
    return redirect(spotify._authorization_ulr())


@app.route('/get-token', methods=["GET"])
def get_token():
    code = request.args.get('code')
    spotify._get_baerer_token(code)
    session['baerer_token'] = f'Bearer {spotify.baerer_token}'
    return redirect("/")


@app.route('/get-user', methods=["GET"])
@valid_token
def get_user():
    user_information = spotify.get_user(
        session.get('baerer_token')
    ).decode('utf-8')
    return jsonify(json.loads(user_information))


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
        host='https://nzh8p1ckm8.execute-api.eu-west-1.amazonaws.com/',
        port=443,
        ssl_context=('cert.pem', 'key.pem')
    )
