from flask import Blueprint, render_template

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
