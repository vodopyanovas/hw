# -*- coding: utf-8 -*-

from app import db

__author__ = 'Anton Vodopyanov'


class BuyAdvert(db.Model):
    __tablename__ = 'buy_advert'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float(6), nullable=False)

    advert_id = db.Column(db.Integer, db.ForeignKey('advert_response.id'))
    responses = db.relationship('AdvertResponse', backref=db.backref('response_to', lazy='dynamic'))

    def __init__(self, title, price, responses):
        self.title = title
        self.price = price
        self.responses = responses

    # def __repr__(self):
    #     return'<Advert %s>' % self.responses


class AdvertResponse(db.Model):
    __tablename__ = 'advert_response'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def __init__(self, text, phone, response_to):
        self.text = text
        self.phone = phone
        self.response_to = response_to









