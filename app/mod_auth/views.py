from flask import Blueprint, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app.mod_auth import LoginForm, RegistrationForm
from app.mod_user.models import UserModel

login_page = Blueprint('login_page', __name__, template_folder='templates')


@login_page.route('/login', methods=['GET', 'POST'])
def login_show():
    if current_user.is_authenticated:
        return redirect(url_for('main_page.show'))

    form = LoginForm()

    if form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login_page.login_show'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main_page.show')
        return redirect(next_page)
    return render_template('auth/login.html', title='Login page', form=form)


logout_page = Blueprint('logout_page', __name__)

@logout_page.route('/logout')
def logout_do():
    logout_user()
    return redirect(url_for('main_page.show'))

register_page = Blueprint('register_page', __name__, template_folder='templates')

@register_page.route('/registeruser', methods=['GET', 'POST'])
def make_register():
    if current_user.is_authenticated:
        return redirect(url_for('main_page.show'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = UserModel(username=form.username.data, password=form.password.data, email=form.email.data)
        user.set_password(form.password.data)
        user.save_to_db()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login_page.login_show'))
    return render_template('auth/register.html', title='Register', form=form)
