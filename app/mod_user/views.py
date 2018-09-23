from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from app.mod_user import UserModel
from app.mod_user.forms import EditProfileForm

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

edit_profile = Blueprint('edit_profile', __name__, template_folder='templates')

@edit_profile.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def profile_show():
    form = EditProfileForm()
    if form.validate_on_submit():
        user = UserModel.find_by_username(current_user.username)
        user.username = form.username.data
        user.about_me = form.about_me.data
        user.save_to_db()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile.profile_show'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('user/edit_profile.html', title='Edit Profile',
                           form=form)