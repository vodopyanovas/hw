# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pygeoip

import config

__author__ = 'Anton Vodopyanov'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance

@app.route('/')
def index():
    from models import UserRequest, LocationModel
    url_address = request.path
    gi = pygeoip.GeoIP('GeoLiteCity.dat')

    if app.debug:
        ip = request.environ.get(
            'X-REMOTE_ADDR', request.remote_addr)
    else:
        ip = request.remote_addr

    # ip = '64.233.161.99'  #test address
    try:
        if request.method == 'GET':
            get_location = gi.record_by_addr(ip)
            location = get_or_create(
                db.session, LocationModel,
                lat=get_location['latitude'],
                lon=get_location['longitude'],
                city=get_location['city'],
                country=get_location['country_name'],
            )
            user_request = UserRequest(ip, url_address, location=location)

            db.session.add(user_request)
            db.session.commit()

        return jsonify({
            'ip': user_request.ip,
            'url': user_request.url,
            'city': user_request.location.city,
            'country': user_request.location.country,
            'latitude': user_request.location.lat,
            'longitude': user_request.location.lon,
        })
    except TypeError:
        return 'Unknown address'

if __name__ == '__main__':
    db.create_all()
    app.run()
