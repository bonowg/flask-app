import os


class Config(object):

    # Define the application directory
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Define the database - we are working with
    fullpath = os.path.join(basedir, 'data.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + fullpath)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    SECRET_KEY = os.environ.get('SECRET_KEY') or 'M2FmYjk0NGJjODc5YTBlY2MwOWU3Nzlm'

    # Statement for enabling the development environment
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2