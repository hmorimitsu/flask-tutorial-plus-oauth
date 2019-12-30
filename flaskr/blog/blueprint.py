from flask import (
    Blueprint, flash, redirect, render_template, url_for
)
from flask_login import current_user, login_required
from werkzeug.exceptions import abort

from flaskr import db
from ..auth.models import User
from .forms import CreateForm, UpdateForm
from .models import Post

bp = Blueprint('blog', __name__)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    form = CreateForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post = Post(current_user.id, title, body)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html', form=form)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    Post.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('blog.index'))


def get_post(id, check_author=True):
    post = Post.query.join(
        User, Post.author_id == User.id).filter(Post.id == id).first()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post.author_id != current_user.id:
        abort(403)

    return post


@bp.route('/')
@login_required
def index():
    posts = Post.query.join(
        User, Post.author_id == User.id).order_by(Post.created.desc()).all()
    return render_template('blog/index.html', posts=posts)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    form = UpdateForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post = Post.query.filter_by(id=id).first()
            post.title = title
            post.body = body
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post, form=form)
