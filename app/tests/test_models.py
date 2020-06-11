#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from flask_restplus import Api
from app.backend.models import User


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

    def test_create_user(self):
        #u = User(id='valentinbus', display_name='valentin bus', photo='url_photo')
        u = db.session.query(User).filter_by(id="jinviuvn").first().id
        assert u == 'jinviuvn'
        # assert u.id == 'valentinb'
        # assert u.display_name == 'valentin bus'
        # assert u.photo == 'url_photo'
    

#     def test_make_unique_nickname(self):
#         u = User(nickname='john', email='john@example.com')
#         db.session.add(u)
#         db.session.commit()
#         nickname = User.make_unique_nickname('john')
#         assert nickname != 'john'
#         u = User(nickname=nickname, email='susan@example.com')
#         db.session.add(u)
#         db.session.commit()
#         nickname2 = User.make_unique_nickname('john')
#         assert nickname2 != 'john'
#         assert nickname2 != nickname

if __name__ == '__main__':
    unittest.main()