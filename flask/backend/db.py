import psycopg2
import os
from sqlalchemy import orm

'''
We have to use ORM like django project to create db's tables etc...
Define a
'''

DB_PASSWORD=os.getenv('DB_PASSWORD')

class Db:
    def __init__(self):
        self.host = 'localhost'
        self.port = 5432
        self.database="spotify_autom_db"
        self.user="valentinbus"
        self.password=DB_PASSWORD
        self.connect_timeout=3

    def _connection(self):
        connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database, 
            user=self.user, 
            password=self.password,
            connect_timeout=self.connect_timeout
        )
        self.connection = connection
        print(connection)

        return "Connection done"


    
db = Db()
db._connection()
