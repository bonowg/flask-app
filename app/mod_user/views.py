from flask import Blueprint, render_template
from flask_login import login_required
from app.mod_user import UserModel


user_profile = Blueprint('user_profile', __name__, template_folder='templates')

@user_profile.route('/user/<username>')
@login_required
def profile_get(username):
    user = UserModel.query.filter_by(username=username).first()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user/user.html', user=user, posts=posts)
