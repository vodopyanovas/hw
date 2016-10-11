# -*- coding: utf-8 -*-

from app import db

__author__ = 'Anton Vodopyanov'


class BuyAdvert(db.Model):
    __tablename__ = 'buy_advert'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(6), nullable=False)

    responses = db.relationship('AdvertResponse', backref='posts', lazy='dynamic')

    def __str__(self):
        return'<Advert %s>' % self.responses
    #
    # def __init__(self, title, price):
    #     self.title = title
    #     self.price = price


class AdvertResponse(db.Model):
    __tablename__ = 'advert_response'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    text = db.Column(db.String(300), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    buyadvert_id = db.Column(db.Integer, db.ForeignKey('buy_advert.id'))



    # def __init__(self, text, phone):
    #     self.text = text
    #     self.phone = phone







