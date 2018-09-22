from flask import Blueprint, render_template, flash, redirect, url_for
from app.mod_items import ItemModel
from app.mod_auth import LoginForm

main_page = Blueprint('main_page', __name__, template_folder='templates')


@main_page.route('/')
@main_page.route('/index')
def show():
    mock_user = {'username': 'Wojtek'}
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
    return render_template('index.html', title='Home', user=mock_user, posts=posts)






