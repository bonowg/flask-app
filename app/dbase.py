import sys
import sqlite3
from flask_sqlalchemy import SQLAlchemy

class ConectDB(object):

    @staticmethod
    def make_connection():
        connection = sqlite3.connect('data.db')
        return connection


db = SQLAlchemy()

if __name__ == '__main__':
    sys.exit()

