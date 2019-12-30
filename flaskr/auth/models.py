from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from .. import db


class User(UserMixin, db.Model):
    __tablename__ = 'site_user'
    id = Column(Integer, primary_key=True)
    external_id = Column(String(40), nullable=False, unique=True)
    name = Column(String(50), nullable=False)

    def __init__(self, external_id=None, name=None):
        self.external_id = external_id
        self.name = name

    def __repr__(self):
        return '<User %r>' % (self.name)
