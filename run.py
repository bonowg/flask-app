#!/home/wojtek/Venv/udemy-flask/bin/python

from app import create_app

if __name__ == '__main__':
    create_app().run(port=5050)
