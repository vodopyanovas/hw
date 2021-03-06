# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

import config

__author__ = 'Anton Vodopyanov'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    from models import Post

    post_form_class = model_form(Post, base_class=FlaskForm, db_session=db.session)

    if request.method == 'POST':

        form = post_form_class(request.form)
        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()
            flash('Post created!')

        else:
            flash('Form is not valid! Post was not created.')

    else:
        form = post_form_class()

    posts = Post.query.all()
    return render_template('index.html', form=form, posts=posts)


if __name__ == '__main__':
    from models import *
    db.create_all()

    app.run()
