from flask import Blueprint, render_template, flash, redirect, url_for
from app.mod_items import ItemModel
from app.mod_auth import LoginForm
from flask_login import current_user


main_page = Blueprint('main_page', __name__, template_folder='templates')


@main_page.route('/')
@main_page.route('/index')
def show():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)
