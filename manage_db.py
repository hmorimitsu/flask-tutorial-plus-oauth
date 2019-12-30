from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from flaskr import db
from flaskr.auth import models as auth_models
from flaskr.blog import models as blog_models

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
