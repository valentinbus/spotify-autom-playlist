#!flask/bin/python
import os
import unittest
import requests

from unittest import mock
from unittest.mock import Mock
from flask import Flask
from config import basedir
from app import db
from app.app import app
from app.backend.models import User

from pprint import pprint


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
        self.app = app.test_client()
        db.create_all()
        u = User(id='jinviuvn', display_name='valentin bus', photo='url_photo')
        db.session.add(u)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @mock.patch('requests.get')
    def test_authent(self, mock_spotify_response):
        mock_spotify_response.return_value.url = 'authorization_url'
        print(requests.get("iunvdivn").url)

        response = self.app.get('authent')
        url = response.get_data().decode('utf-8')
        print(f"URL:::authorization_url")
        print(f"URL:::{url[0]}")
        assert response.status_code == 200
        assert url == "authorization_url"


if __name__ == '__main__':
    unittest.main()
