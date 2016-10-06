# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators


__author__ = 'Anton Vodopyanov'


class PostForm(FlaskForm):
    text = StringField(validators=[validators.Length(min=5, max=140)])
    download_file = BooleanField(label='download file', default=False)
