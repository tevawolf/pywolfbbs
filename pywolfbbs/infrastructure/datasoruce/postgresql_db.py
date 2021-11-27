import os

import psycopg2
from flask import g

# DATABASE_HEROKU = os.environ.get('DATABASE_URL')

DATABASE_LOCAL = 'host=127.0.0.1 port=5432 dbname=pywolfbbs user=tevawolf password=teVa0210'


def get_postgres():
    db = getattr(g, '_database', None)
    if db is None:
        # db = g._database = psycopg2.connect(DATABASE_HEROKU)
        db = g._database = psycopg2.connect(DATABASE_LOCAL)
    return db


def close_postgres_connection(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
