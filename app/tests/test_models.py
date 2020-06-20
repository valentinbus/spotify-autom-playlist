#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from flask_restplus import Api
from app.backend.models import (
    User,
    Track,
    Category,
    CategoryTrack,
    Playlist,
    TrackPlaylist
)


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('TEST_DATABASE_URL')
        self.app = app.test_client()
        db.create_all()
        u = User(id='jinviuvn', display_name='valentin bus', photo='url_photo')
        track = Track(id='track id', name='Song', artist='bob marley')
        category = Category(name='category name')

        db.session.add(u)
        db.session.add(track)
        db.session.add(category)
        db.session.commit()

        playlist = Playlist(
            id='12345',
            name='Loved Tracks',
            user_id='jinviuvn',
            spotify_id='1234'
        )

        db.session.add(playlist)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_query_user(self):
        u = db.session.query(User).filter_by(id="jinviuvn").first()
        self.assertEqual(u.id, 'jinviuvn')
        assert u.display_name == 'valentin bus'
        assert u.photo == 'url_photo'

    def test_create_user(self):
        u = User(
            id='aaaaaa',
            display_name='mathilde pelouzet',
            photo="url_photo"
        )
        db.session.add(u)
        db.session.commit()

        self.assertEqual(
            db.session.query(User).filter_by(id='aaaaaa').first().display_name,
            "mathilde pelouzet"
        )

    def test_create_playlist(self):
        playlist = Playlist(
            id='1234',
            name='Loved Tracks',
            user_id='jinviuvn',
            spotify_id='1234'
        )

        db.session.add(playlist)
        db.session.commit()

        playlist = db.session.query(Playlist).filter_by(id='1234').first()
        self.assertEqual(playlist.id, 1234)
        self.assertEqual(playlist.name, 'Loved Tracks')
        self.assertEqual(playlist.user_id, 'jinviuvn')
        self.assertEqual(playlist.spotify_id, '1234')

    def test_create_track_playlist(self):
        playlist_id = (
            db.session.query(Playlist)
            .filter_by(id='12345')
            .first().id
        )
        track_id = (
            db.session.query(Track)
            .filter_by(id='track id')
            .first().id
        )

        track_playlist = TrackPlaylist(
            id=1,
            playlist_id=playlist_id,
            track_id=track_id
        )

        db.session.add(track_playlist)
        db.session.commit()

        query = db.session.query(TrackPlaylist).filter_by(id=1).first()

        self.assertEqual(
            query.playlist_id,
            12345
        )

        self.assertEqual(
            query.track_id,
            "track id"
        )

    def test_create_track(self):
        track = Track(
            id="track id2",
            name="song",
            artist="billy boy"
        )

        db.session.add(track)
        db.session.commit()

        query = db.session.query(Track).filter_by(id='track id2').first()

        self.assertEqual(
            query.name,
            "song"
        )
        self.assertEqual(
            query.artist,
            "billy boy"
        )

    def test_create_category(self):
        category = Category(
            name="category name"
        )

        db.session.add(category)
        db.session.commit()

        query = (
            db.session.query(Category)
            .filter_by(name="category name")
            .first()
        )

        self.assertEqual(
            query.name,
            "category name"
        )

    def test_category_track(self):
        category_id = (
            db.session.query(Category)
            .filter_by(name="category name")
            .first().id
        )

        category_track = CategoryTrack(
            track_id="track id",
            category_id=category_id
        )

        db.session.add(category_track)
        db.session.commit()

        query = (
            [
                element for element
                in db.session.query(CategoryTrack).all()
            ][0]
        )

        self.assertEqual(
            query.track_id,
            "track id"
        )

        self.assertEqual(
            query.category_id,
            category_id
        )


if __name__ == '__main__':
    unittest.main()
