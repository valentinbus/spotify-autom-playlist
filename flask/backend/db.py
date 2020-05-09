import psycopg2
import os
from sqlalchemy import orm

'''
We have to use ORM like django project to create db's tables etc...
'''

print('okkkkk')

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="spotify_autom_db", 
    user="valentinbus", 
    password=os.getenv('DB_PASSWORD'),
    connect_timeout=3
)

print(conn)

