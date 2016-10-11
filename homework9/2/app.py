# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms_sqlalchemy.orm import model_form
from sqlalchemy.exc import IntegrityError


import config

__author__ = 'Anton Vodopyanov'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
def index():
    from models import BuyAdvert

    post_buy_advert = model_form(BuyAdvert, base_class=FlaskForm, db_session=db.session)

    if request.method == 'POST':

        form = post_buy_advert(request.form)
        if form.validate():
            try:
                buy_adv = BuyAdvert(**form.data)
                db.session.add(buy_adv)
                db.session.commit()
                flash('Post created!')

            except IntegrityError as ex:
                db.session.rollback()
                flash(ex)

        else:
            flash('Form is not valid! Post was not created.')

    else:
        form = post_buy_advert()

    posts = BuyAdvert.query.all()

    return render_template('index.html', form=form, postss=posts)


@app.route('/response', methods=['GET', 'POST'])
def response():
    from models import AdvertResponse
    post_response = model_form(AdvertResponse, base_class=FlaskForm, db_session=db.session)

    if request.method == 'POST':
        form = post_response(request.form)
        if form.validate():
            try:
                adv_response = AdvertResponse(**form.data)
                db.session.add(adv_response)
                db.session.commit()
                flash('Response created!')

            except IntegrityError as ex:
                db.session.rollback()
                flash(ex)

        else:
            flash('Form is not valid! Post was not created.')

    else:
        form = post_response()

    posts = AdvertResponse.query.all()

    return render_template('response.html', form=form, posts=posts)


if __name__ == '__main__':
    from models import *
    db.create_all()

    app.run()
