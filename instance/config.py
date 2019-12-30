import os

DEBUG = True

CSRF_ENABLED = True

# Replace the keys below by a secret random key!
CSRF_SESSION_KEY = 'secret'
SECRET_KEY = 'secret'
# CSRF_SESSION_KEY = os.environ['SECRET_KEY']
# SECRET_KEY = os.environ['SECRET_KEY']

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = 'postgres://my_user:my_password@localhost:5432/flaskr'
DATABASE_URL = 'sqlite:///{}/flaskr.db'.format(BASE_DIR)

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

# You need to export the Github and/or Google environment variables
# before starting the Flask server.
try:
    GITHUB_OAUTH_CLIENT_ID = os.environ['GITHUB_OAUTH_CLIENT_ID']
    GITHUB_OAUTH_CLIENT_SECRET = os.environ['GITHUB_OAUTH_CLIENT_SECRET']
    GITHUB_FOUND = True
except KeyError:
    GITHUB_FOUND = False
    print('WARNING! '
          'Could not find Github OAUTH keys. Github login cannot be used')

try:
    GOOGLE_OAUTH_CLIENT_ID = os.environ['GOOGLE_OAUTH_CLIENT_ID']
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ['GOOGLE_OAUTH_CLIENT_SECRET']
    GOOGLE_FOUND = True
except KeyError:
    GOOGLE_FOUND = False
    print('WARNING! '
          'Could not find Google OAUTH keys. Google login cannot be used')
