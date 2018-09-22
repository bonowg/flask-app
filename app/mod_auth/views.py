from flask import Blueprint, flash, redirect, render_template, url_for
from app.mod_auth import LoginForm

login_page = Blueprint('login_page', __name__, template_folder='templates')


@login_page.route('/login', methods=['GET', 'POST'])
def login_show():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('main_page.show'))
    return render_template('auth/login.html', title='Login page', form=form)

