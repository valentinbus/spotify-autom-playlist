from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    display_name = db.Column(db.String(140))
    photo = db.Column(db.String(140))

    def __repr__(self):
        return '<User {}>'.format(self.id)   

    # def __init__(self, id, display_name, photo):
    #     self.id = id
    #     self.display_name = display_name 
    #     self.photo = photo

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    user_id = db.Column(db.String(64), db.ForeignKey('user.id'))
    spotify_id = db.Column(db.String(140))

    def __repr__(self):
        return '<Playlist {}>'.format(self.name)

    # def __init__(self, id, name, user_id, spotify_id):
    #     self.id = id
    #     self.name = name
    #     self.user_id = user_id
    #     self.spotify_id = spotify_id

class TrackPlaylist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
    track_id = db.Column(db.String(140), db.ForeignKey('track.id'))

    def __repr__(self):
        return '<TrackPlaylist {}>'.format(self.id)

    # def __init__(self, id, playlist_id, track_id):
    #     self.id = id
    #     self.playlist_id = playlist_id
    #     self.track_id = track_id

class Track(db.Model):
    id = db.Column(db.String(140), primary_key=True)
    name = db.Column(db.String(140))
    artist = db.Column(db.String(140))

    def __repr__(self):
        return '<Track {}>'.format(self.name)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))

    def __repr__(self):
        return '<Category {}>'.format(self.name)

class CategoryTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.String(140), db.ForeignKey('track.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<CategoryTrack {}>'.format(self.name)
