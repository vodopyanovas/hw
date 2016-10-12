# -*- coding: utf-8 -*-

from datetime import date

from app import db

__author__ = 'Anton Vodopyanov'


class Post(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    birthday = db.Column(db.Date, default=date.today(), nullable=False)
    age = db.Column(db.Integer, )

    def __init__(self, username='', name='', age=0, birthday=None,):
        self.username = username
        self.name = name
        self.birthday = birthday
        self.age = (date.today() - birthday).days // 365







