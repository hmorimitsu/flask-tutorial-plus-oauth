from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .. import db


class Post(db.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('site_user.id'), nullable=False)
    created = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False)
    title = Column(String(50), nullable=False)
    body = Column(String(500), nullable=False)
    author = relationship('User')

    def __init__(self, author_id=None, title=None, body=None):
        self.author_id = author_id
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Title %r>' % (self.title)
