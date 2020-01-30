import pytest

from flask.backend.spotify import Spotify

spotify = Spotify()
d = {
    "display_name": "valentinoiho",
    "external_urls": {
        "spotify": "https://open.spotify.com/user/valentinoiho"
    },
    "followers": {
        "href": "ok",
        "total": 4
    },
    "href": "https://api.spotify.com/v1/users/valentinoiho",
    "id": "valentinoiho",
    "images": [
        {
            "height": "null",
            "url": "https://profile-images.scdn.co/images/userprofile/default/788ee6f4ef0984e9a9f37705c364572b1f1efd45",
            "width": "null"
        }
    ],
    "type": "user",
    "uri": "spotify:user:valentinoiho"
}


def test_get_user_informations(monkeypatch):
    class MockRequestGet:
        def __init__(self, url, headers):
            pass

        def json(self):
            return d

    monkeypatch.setattr("requests.get", MockRequestGet)
    assert(
        spotify.get_user("token") == d
    )


def test_get_tracks(monkeypatch):
    result = {
        "href": list(),
        "items": list(),
        "limit": 50,
        "next": list(),
        "offset": 0,
        "previous": None,
        "total": 1
    }

    class MockRequestGet:
        def __init__(self, url, headers, params):
            pass

        def json(self):
            return result

    monkeypatch.setattr("requests.get", MockRequestGet)
    assert(
        spotify.get_tracks("token") == [result]
    )
