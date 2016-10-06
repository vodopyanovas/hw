# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, send_file, redirect
from form import PostForm
from models import PostModel

import config


__author__ = 'Anton Vodopyanov'


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = PostForm(request.form)
        user_input = PostModel(form.data)
        if form.validate_on_submit():
            user_input.save_text()
            user_input.get_qr()
            if form.data['download_file']:
                return redirect('/get_file')
            else:
                return redirect('/qr')

    else:
        form = PostForm()

    return render_template('index.html', form=form)


@app.route('/qr', methods=['GET'])
def send():
    return send_file('tmp/qr.png')


@app.route('/get_file', methods=['GET'])
def send_txt():
    return send_file('tmp/my_text.txt', as_attachment=True)

if __name__ == '__main__':
    app.run()
