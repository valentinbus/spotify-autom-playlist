#!flask/bin/python
import os
import unittest
import requests
import json

from unittest import mock
from flask import Flask
from config import basedir
from app import db
from app.app import app
from app.backend.spotify import Spotify
from app.backend.models import (
    User,
    Track,
    Category,
    CategoryTrack,
    Playlist,
    TrackPlaylist
)

from pprint import pprint


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
        self.app = app.test_client()
        db.create_all()
        u = User(id='valentinoiho',
                 display_name='valentin bus', photo='url_photo')
        track = Track(id="track id", name='Song', artist='bob marley')
        category = Category(name='category name')

        db.session.add(u)
        db.session.add(track)
        db.session.add(category)
        db.session.commit()

        playlist = Playlist(
            id='12345',
            name='Loved Tracks',
            user_id='valentinoiho',
            spotify_id='1234'
        )

        playlist2 = Playlist(
            id='123456',
            name='category name',
            user_id='valentinoiho',
            spotify_id='1234'
        )

        db.session.add(playlist)
        db.session.add(playlist2)
        db.session.commit()

        track_playlist = TrackPlaylist(
            playlist_id=12345,
            track_id="track id"
        )

        category_track = CategoryTrack(
            track_id="track id",
            category_id=1
        )

        db.session.add(track_playlist)
        db.session.add(category_track)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @mock.patch("requests.get")
    def test_authorization(self, mock_request):
        class NewResponse:
            def __init__(self):
                self.url = "url"

        mock_request.return_value = NewResponse()

        self.assertEqual(Spotify()._authorization_ulr(), "url")

    @mock.patch("json.loads")
    def test_get_baerer_token(self, mock_request):
        mock_request.return_value = {'access_token': 'true'}

        self.assertEqual(Spotify()._get_baerer_token('code'), 'localhost')

    @mock.patch("requests.get")
    def test_check_token(self, mock_request):

        mock_request.return_value.json.return_value = 'true'
        self.assertEqual(Spotify()._check_token('token'), 'true')

    @mock.patch("requests.get")
    def test_user_id(self, mock_response):
        mock_response.return_value.json.return_value = {
            'id': '09090909',
            'display_name': 'mathilde pelouzet',
            "images": [
                {
                    "url": "url_photo",
                }
            ]
        }

        spotify = Spotify()
        self.assertEqual(spotify._get_user_id('token'), '09090909')

        user = db.session.query(User).filter_by(id='09090909').first()

        self.assertEqual(user.id, '09090909')
        self.assertEqual(user.display_name, 'mathilde pelouzet')
        self.assertEqual(user.photo, 'url_photo')

    @mock.patch("requests.get")
    def test_init_loved_track(self, mock_response):
        mock_response.return_value.json.return_value = {
            'total': 200,
            'items': [
                {
                    "track": {
                        'id': 'id1',
                        'name': 'name1',
                        'artists': [
                            {
                                'id': 'artist1'
                            }
                        ]
                    }
                },
                {
                    "track": {
                        'id': 'id2',
                        'name': 'name2',
                        'artists': [
                            {
                                'id': 'artist2'
                            }
                        ]
                    }
                },
            ]
        }

        self.assertEqual(
            Spotify()._init_loved_track('token', 'valentinoiho'),
            [
                {
                    'id': 'id1',
                    'name': 'name1',
                    'artist': 'artist1'
                },
                {
                    'id': 'id2',
                    'name': 'name2',
                    'artist': 'artist2'
                },
                {
                    'id': 'id1',
                    'name': 'name1',
                    'artist': 'artist1'
                },
                {
                    'id': 'id2',
                    'name': 'name2',
                    'artist': 'artist2'
                },
                {
                    'id': 'id1',
                    'name': 'name1',
                    'artist': 'artist1'
                },
                {
                    'id': 'id2',
                    'name': 'name2',
                    'artist': 'artist2'
                },
                {
                    'id': 'id1',
                    'name': 'name1',
                    'artist': 'artist1'
                },
                {
                    'id': 'id2',
                    'name': 'name2',
                    'artist': 'artist2'
                },
                {
                    'id': 'id1',
                    'name': 'name1',
                    'artist': 'artist1'
                },
                {
                    'id': 'id2',
                    'name': 'name2', 'artist': 'artist2'
                }
            ]
        )

        self.assertEqual(
            db.session.query(Track).filter_by(name='name1').first().id,
            'id1'
        )

        self.assertEqual(
            db.session.query(Track).filter_by(name='name2').first().id,
            'id2'
        )

    @mock.patch("requests.get")
    def test_init_category(self, mock_response):
        """
        Test with a non existing category
        """
        mock_response.return_value.json.return_value = {
            'genres': [
                "genre"
            ]
        }

        self.assertEqual(
            Spotify()._init_category('token', 'valentin'),
            [
                {
                    'category_id': 2,
                    'category_name': 'genre'
                },
                {
                    'category_id': 2, 'category_name': 'genre'
                }
            ]
        )

    def test_init_first_playlist(self):
        self.assertEqual(
            Spotify()._init_first_playlist(
                'token',
                'valentinoiho',
                'track id'
            ),
            {
                'message': 'Good !',
                'playlist': {
                    'name': 'Loved Tracks',
                    'id': 12345
                }
            }
        )

        # If playlist already exists
        playlist = Playlist(user_id="valentinoiho", name="Loved Tracks")
        db.session.add(playlist)
        db.session.commit()

        self.assertEqual(
            Spotify()._init_first_playlist(
                'token',
                'valentinoiho',
                'track id'
            ),
            {
                'message': 'Good !',
                'playlist': {
                    'name': 'Loved Tracks',
                    'id': 12345
                }
            }
        )

    @mock.patch("requests.post")
    def test_add_tracks(self, mock_response):
        mock_response.return_value = "ok"

        self.assertEqual(
            Spotify()._add_track(
                token="token",
                playlist_name='category name',
                playlist_id='playlist id',
                user_id='valentinoiho'
            ),
            {'ok': 'super'}
        )

    def test_get_suggest_playlist(self):
        self.assertEqual(
            Spotify().suggest_playlist("valentinoiho"),
            {'relevant_category': [{'id': 1, 'name': 'category name'}]}
        )


if __name__ == '__main__':
    unittest.main()
