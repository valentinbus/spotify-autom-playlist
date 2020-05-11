from app import app, db
from app.backend.models import User, Post

'''
Run `flask shell`
'''
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
