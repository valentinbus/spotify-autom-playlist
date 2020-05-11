import os
basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = "localhost"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

