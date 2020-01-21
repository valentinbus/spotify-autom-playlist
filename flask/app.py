from flask import (
    Flask,
    request,
    render_template,
    jsonify,
    Response,
    make_response,
    redirect
)
from backend.spotify import Spotify
from flask_cors import CORS, cross_origin

import json


spotify = Spotify()

app = Flask(__name__)
CORS(app)

@app.route('/', methods=["GET"])
def home():
    return Response("Vous êtes dans l'application :)")

@app.route('/authent', methods=["GET"])
def authent():
    return redirect(spotify._authorization_ulr())

@app.route('/get-token', methods=["GET"])
def get_token():
    code = request.args.get('code')
    return redirect("/")

@app.route('/get-baerer', methods=["GET"])
def baerer_redirect():
    return Response("ok")



if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=80,
    )