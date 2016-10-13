from app import db
import datetime


class UserRequest(db.Model):
    __tablename__ = 'visit'
    id = db.Column('id', db.Integer, primary_key=True)
    date_create = db.Column('date', db.DateTime, default=datetime.datetime.now())
    ip_address = db.Column('ip', db.String(15))
    url_link = db.Column('url', db.String)

    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    location = db.relationship('LocationModel', backref=db.backref('requests', lazy='dynamic'))

    def __init__(self, ip, url, location=None):
        self.ip = ip
        self.url = url
        self.location = location


class LocationModel(db.Model):
    __tablename__ = 'location'
    id = db.Column('id', db.Integer, primary_key=True)
    lat = db.Column('lat', db.Float)
    lon = db.Column('lon', db.Float)
    city = db.Column('city', db.String(20))
    country = db.Column('country', db.String(100))

    def __init__(self, lat=None, lon=None, city=None, country=None):
        self.lat = lat
        self.lon = lon
        self.city = city
        self.country = country


