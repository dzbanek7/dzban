#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  views.py

from flask import Flask
from flask import render_template, request
from modele import Kategoria, Pytanie, Odpowiedz


app = Flask(__name__)

#widok domyślny
@app.route("/")
def hello():
    return render_template('index.html')
    
@app.route("/lista")
def lista():
    pytania = Pytanie.select()
    return render_template('lista.html', pytania=pytania)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
