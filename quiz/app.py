#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
from flask import g
from modele import *
from views import *

app.config.update(dict(
    SECRET_KEY='bardzosekretnyklucz',
    TITLE='Aplikacja Quiz',
))

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)
