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
def index():
    from models import Student

    post_form_class = model_form(Student, base_class=FlaskForm, db_session=db.session)

    if request.method == 'POST':
        form = post_form_class(request.form)
        if form.validate():
            try:
                post = Student(**form.data)
                db.session.add(post)
                db.session.commit()
                flash('Student created!')

            except IntegrityError:
                db.session.rollback()
                flash("User {} is already exists".format(post.studentID))

        else:
            flash('Form is not valid! Student was not created.')

    else:
        form = post_form_class()
    posts = Student.query.all()
    # posts = Student.query.filter(Student.age > 17).all()

    return render_template('index.html', form=form, posts=posts)


if __name__ == '__main__':
    from models import *
    db.create_all()

    app.run()
