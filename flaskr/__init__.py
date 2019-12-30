import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.db'),
    )
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    db.init_app(app)
    login_manager.init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if app.config['GITHUB_FOUND']:
        print('GITHUB_FOUND')
        from flask_dance.contrib.github import make_github_blueprint
        github_bp = make_github_blueprint(redirect_url='/auth/github_callback')
        app.register_blueprint(github_bp, url_prefix='/login')

    if app.config['GOOGLE_FOUND']:
        print('GOOGLE_FOUND')
        from flask_dance.contrib.google import make_google_blueprint
        google_bp = make_google_blueprint(redirect_url='/auth/google_callback')
        app.register_blueprint(google_bp, url_prefix='/login')

    from .auth import blueprint as auth_bp
    app.register_blueprint(auth_bp.bp)

    from .blog import blueprint as blog_bp
    app.register_blueprint(blog_bp.bp)
    app.add_url_rule('/', endpoint='index')

    return app
