from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    playlist = db.Column(db.Integer, db.ForeignKey('playlist.id'))

    def __repr__(self):
        return '<User {}>'.format(self.id)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    id_user = db.Column(db.String(100), db.ForeignKey('user.id'))
    id_track = db.Column(db.Integer, db.ForeignKey('track.id'))
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Playlist {}>'.format(self.name)
        
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return '<Playlist {}>'.format(self.name)

class Category_Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_track = db.Column(db.Integer, db.ForeignKey('track.id'))
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'))

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return '<Playlist {}>'.format(self.name)

class Track_Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_track = db.Column(db.Integer, db.ForeignKey('track.id'))
    id_playlist = db.Column(db.Integer, db.ForeignKey('playlist.id'))
