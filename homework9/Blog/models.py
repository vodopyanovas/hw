# -*- coding: utf-8 -*-

from datetime import datetime

from app import db

__author__ = 'sobolevn'
__author__ = 'Anton Vodopyanov'


class Post(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    user = db.Column(db.String(20), unique=True, name='User', nullable=False)
    title = db.Column(db.String(140), unique=True, nullable=False)
    content = db.Column(db.String(3000), nullable=False)

    date_created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, title='', content='', user=None,
                 date_created=None,):
        self.title = title
        self.content = content
        self.user = user

        if date_created is not None:
            self.date_created = date_created
