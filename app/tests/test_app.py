#!flask/bin/python
import os
import unittest
import requests

from unittest import mock
from unittest.mock import Mock, MagicMock
from flask import Flask
from config import basedir
from app import db
from app.app import app
from app.backend.spotify import Spotify
from app.backend.models import User

from pprint import pprint


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
        self.app = app.test_client()
        db.create_all()
        u = User(id='valentinoiho', display_name='valentin bus', photo='url_photo')
        db.session.add(u)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @mock.patch('__main__.Spotify._authorization_ulr')
    def test_authent(self, mock_spotify_response):
        mock_spotify_response.return_value = "authorization_url"
        response = self.app.get('authent')
        url = response.get_data()

        assert response.status_code == 200
        self.assertEqual(url, b'"authorization_url"\n')

    @mock.patch('__main__.Spotify._get_user_id')
    def test_get_token(self, mock_spotify):
        mock_spotify.return_value = 'valentinoiho'

        response = self.app.get('get-token', data="code")

        assert response.status_code == 200
        self.assertEqual(response.get_data(), b'{"jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoidmFsZW50aW5vaWhvIiwiYmFlcmVyX3Rva2VuIjoiQmVhcmVyIE5vbmUifQ.j_0jkZGXA2Vv-m3zkpWzefzzAyimfpKHDj5gaNzgP2Q"}\n')

    @mock.patch("__main__.Spotify._check_token")
    def test_check_token(self, mock_check_token):
        mock_check_token.return_value = "JWT TOKEN"

        response = self.app.get(
            'check-token',
            headers={
                'jwt_token': 'youpi'
            }
        )

        assert response.status_code == 200
        self.assertEqual(
            response.get_data(),
            b'{"error": "Not enough segments:::Check Jwt token"}\n'
        )

        response = self.app.get(
            'check-token',
            headers={
                'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                '.eyJ1c2VyX2lkIjoidmFsZW50aW5vaWhvIiwiYmFlcmVy'
                'X3Rva2VuIjoiQmVhcmVyIE5vbmUifQ.j_0jkZGXA2Vv-'
                'm3zkpWzefzzAyimfpKHDj5gaNzgP2Q'
            }
        )

        self.assertEqual(response.get_data(), b'"JWT TOKEN"\n')

    @mock.patch('__main__.Spotify.init_db')
    def test_init_db(self, mock_spotify):

        mock_spotify.return_value = "response ok"

        response = self.app.put(
            'init-db',
            headers={
                'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                '.eyJ1c2VyX2lkIjoidmFsZW50aW5vaWhvIiwiYmFlcmVy'
                'X3Rva2VuIjoiQmVhcmVyIE5vbmUifQ.j_0jkZGXA2Vv-'
                'm3zkpWzefzzAyimfpKHDj5gaNzgP2Q'
            }
        )

        assert response.status_code == 200
        self.assertEqual(response.get_data(), b'"response ok"\n')

    @mock.patch("__main__.Spotify.clear_db")
    def test_clear_db(self, mock_spotify):
        mock_spotify.return_value = "response ok"

        response = self.app.delete(
            'clear-db',
            headers={
                'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                '.eyJ1c2VyX2lkIjoidmFsZW50aW5vaWhvIiwiYmFlcmVy'
                'X3Rva2VuIjoiQmVhcmVyIE5vbmUifQ.j_0jkZGXA2Vv-'
                'm3zkpWzefzzAyimfpKHDj5gaNzgP2Q'
            }
        )

        assert response.status_code == 200
        self.assertEqual(response.get_data(), b'"response ok"\n')

    @mock.patch("__main__.Spotify.get_tracks")
    def test_get_tracks(self, mock_spotify):
        mock_spotify.return_value = "response ok"

        response = self.app.get(
            'get-tracks',
            headers={
                'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                '.eyJ1c2VyX2lkIjoidmFsZW50aW5vaWhvIiwiYmFlcmVy'
                'X3Rva2VuIjoiQmVhcmVyIE5vbmUifQ.j_0jkZGXA2Vv-'
                'm3zkpWzefzzAyimfpKHDj5gaNzgP2Q'
            }
        )

        assert response.status_code == 200
        self.assertEqual(response.get_data(), b'"response ok"\n')

    @mock.patch("__main__.Spotify.get_playlist")
    def test_get_playlist(self, mock_spotify):
        mock_spotify.return_value = "response ok"

        response = self.app.get(
            'get-playlist',
            headers={
                'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                '.eyJ1c2VyX2lkIjoidmFsZW50aW5vaWhvIiwiYmFlcmVy'
                'X3Rva2VuIjoiQmVhcmVyIE5vbmUifQ.j_0jkZGXA2Vv-'
                'm3zkpWzefzzAyimfpKHDj5gaNzgP2Q'
            }
        )

        assert response.status_code == 200
        self.assertEqual(response.get_data(), b'"response ok"\n')

    @mock.patch("__main__.Spotify.get_user")
    def test_get_user(self, mock_spotify):
        mock_spotify.return_value = "response ok"

        response = self.app.get(
            'get-user',
            headers={
                'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                '.eyJ1c2VyX2lkIjoidmFsZW50aW5vaWhvIiwiYmFlcmVy'
                'X3Rva2VuIjoiQmVhcmVyIE5vbmUifQ.j_0jkZGXA2Vv-'
                'm3zkpWzefzzAyimfpKHDj5gaNzgP2Q'
            }
        )

        assert response.status_code == 200
        self.assertEqual(response.get_data(), b'"response ok"\n')

    @mock.patch("__main__.Spotify.create_playlist")
    def test_get_create_playlist(self, mock_spotify):
        mock_spotify.return_value = "response ok"

        response = self.app.post(
            'create-playlist',
            headers={
                'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                '.eyJ1c2VyX2lkIjoidmFsZW50aW5vaWhvIiwiYmFlcmVy'
                'X3Rva2VuIjoiQmVhcmVyIE5vbmUifQ.j_0jkZGXA2Vv-'
                'm3zkpWzefzzAyimfpKHDj5gaNzgP2Q'
            },
            data={
                'category_id': 'none'
            }
        )

        assert response.status_code == 200
        self.assertEqual(response.get_data(), b'"response ok"\n')


if __name__ == '__main__':
    unittest.main()
