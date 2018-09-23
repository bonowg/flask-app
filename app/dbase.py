import sqlite3
import sys

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


class ConectDB(object):

    @staticmethod
    def make_connection():
        connection = sqlite3.connect('data.db')
        return connection


db = SQLAlchemy()
login_manager = LoginManager()

if __name__ == '__main__':
    sys.exit()

