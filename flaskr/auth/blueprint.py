from flask import (
    Blueprint, current_app, flash, g, redirect, render_template, url_for
)
from flask_dance.contrib.github import github
from flask_dance.contrib.google import google
from flask_login import login_user, logout_user
from oauthlib.oauth2.rfc6749.errors import InvalidGrantError, TokenExpiredError

from flaskr import db, login_manager
from .models import User
from .forms import GithubForm, GoogleForm

bp = Blueprint('auth', __name__, url_prefix='/auth')


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.filter_by(id=user_id).first()
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to see this page')
    return redirect(url_for('auth.login'))


# Handling multiple forms, as proposed on
# https://stackoverflow.com/questions/18290142/multiple-forms-in-a-single-page-using-flask-and-wtforms
@bp.route('/login', methods=('GET', 'POST'))
def login():
    github_form = GithubForm()
    google_form = GoogleForm()

    return render_template(
        'auth/login.html', github_form=github_form, google_form=google_form,
        is_github_found=current_app.config['GITHUB_FOUND'],
        is_google_found=current_app.config['GOOGLE_FOUND'])


@bp.route('/github_login', methods=('GET', 'POST'))
def github_login():
    github_form = GithubForm()
    google_form = GoogleForm()

    if github_form.validate_on_submit():
        if not github.authorized:
            return redirect(url_for('github.login'))
        else:
            return github_callback()

    return render_template(
        'auth/login.html', github_form=github_form, google_form=google_form,
        is_github_found=current_app.config['GITHUB_FOUND'],
        is_google_found=current_app.config['GOOGLE_FOUND'])


@bp.route('/github_callback', methods=('GET', 'POST'))
def github_callback():
    resp = github.get('/user')
    if resp.ok:
        resp = resp.json()
        external_id = 'github_' + str(resp['id'])
        user = User.query.filter_by(external_id=external_id).first()
        if user is None:
            user = User(external_id, resp['name'][:50])
            db.session.add(user)
            db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('index'))

    github_form = GithubForm()
    google_form = GoogleForm()
    return render_template(
        'auth/login.html', github_form=github_form, google_form=google_form,
        is_github_found=current_app.config['GITHUB_FOUND'],
        is_google_found=current_app.config['GOOGLE_FOUND'])


@bp.route('/google_login', methods=('GET', 'POST'))
def google_login():
    github_form = GithubForm()
    google_form = GoogleForm()

    if google_form.validate_on_submit():
        if not google.authorized:
            return redirect(url_for('google.login'))
        else:
            return google_callback()

    return render_template(
        'auth/login.html', github_form=github_form, google_form=google_form,
        is_github_found=current_app.config['GITHUB_FOUND'],
        is_google_found=current_app.config['GOOGLE_FOUND'])


@bp.route('/google_callback', methods=('GET', 'POST'))
def google_callback():
    # Workaround to handle oauth errors as proposed on
    # https://github.com/singingwolfboy/flask-dance/issues/35
    try:
        if 'num_google_tries' not in g:
            g.num_google_tries = 0
        else:
            g.num_google_tries += 1

        resp = google.get('/oauth2/v1/userinfo')
    except (InvalidGrantError, TokenExpiredError) as e:
        # Only try once to avoid infinite loops
        if g.num_google_tries < 1:
            return redirect(url_for("google.login"))
        else:
            raise e
    if resp.ok:
        resp = resp.json()
        external_id = 'google_' + str(resp['id'])
        user = User.query.filter_by(external_id=external_id).first()
        if user is None:
            user = User(external_id, resp['name'][:50])
            db.session.add(user)
            db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('index'))

    github_form = GithubForm()
    google_form = GoogleForm()
    return render_template(
        'auth/login.html', github_form=github_form, google_form=google_form,
        is_github_found=current_app.config['GITHUB_FOUND'],
        is_google_found=current_app.config['GOOGLE_FOUND'])


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
