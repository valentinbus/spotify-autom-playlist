from app import app, db
# from app.backend.models import (
#     User, 
#     Category, 
#     Category_Tracks, 
#     Playlist, 
#     Track, 
#     Track_Playlist
# )

from app.backend.models import User, Playlist, Track, TrackPlaylist
'''
Run `flask shell`
'''
# @app.shell_context_processor
# def make_shell_context():
#     return {
#         'db': db, 
#         'User': User, 
#         'Category': Category,
#         'Category_Tracks': Category_Tracks, 
#         'Playlist': Playlist,
#         'Track': Track,
#         'Track_Playlist': Track_Playlist
#     }

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'User': User,
        'Playlist': Playlist, 
        'Track': Track, 
        'TrackPlaylist': TrackPlaylist
    }