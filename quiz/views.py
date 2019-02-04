#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  views.py
from flask import Flask
from flask import render_template, request, flash, redirect, url_for
from modele import Kategoria, Pytanie, Odpowiedz
from forms import *


app = Flask(__name__)

# widok domyślny
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/lista")
def lista():
    pytania = Pytanie.select()
    return render_template('lista.html', pytania=pytania)

@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    print(request.form)
    
    if request.method == 'POST':
        wynik = 0
        for pid, oid in request.form.items():
            if Odpowiedz().get(Odpowiedz.id == int(oid)).odpok:
                wynik += 1
        
        flash('Poprawnych odpowiedzi: {}'.format(wynik), 'info')
        return redirect(url_for('index'))
                
    pytania = Pytanie.select().join(Odpowiedz).distinct()
    return render_template('quiz.html', pytania=pytania)

def flash_errors(form):
    """Odczytanie wszystkich błędów formularza i przygotowanie komunikatów"""
    for field, errors in form.errors.items():
        for error in errors:
            if type(error) is list:
                error = error[0]
            flash("Błąd: {}. Pole: {}".format(
                error,
                getattr(form, field).label.text))

@app.route("/dodaj", methods=['GET', 'POST'])
def dodaj():
    """Dodawanie pytań i odpowiedzi"""
    form = DodajForm()
    form.kategoria.choices = [(k.id, k.kategoria) for k in Kategoria.select()]
    
    if form.validate_on_submit():
        print(form.data)
        p = Pytanie(pytanie=form.pytanie.data, kategoria=form.kategoria.data)
        p.save()
        for o in form.odpowiedzi.data:
            odp = Odpowiedz(odpowiedz=o['odpowiedz'],
                            pytanie=p.id,
                            odpok=int(o['odpok']))
            odp.save()
        flash("Dodano pytanie: {}".format(form.pytanie.data))
        return redirect(url_for('lista'))
        
    elif request.method == 'POST':
        flash_errors(form)
    
    return render_template('dodaj.html', form=form)

def get_or_404(pid):
    try:
        p = Pytanie.get_by_id(pid)
        return p
    except Pytanie.DoesNotExist:
        abort(404)
        
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/usun/<int:pid>", methods=['GET', 'POST'])
def usun():
    """Usuwanie pytań i odpowiedzi"""
    p = get_or_404(pid)
    if request.method == 'Post':
        pass   
    return render_template("pytanie_usun.html", pytanie=p)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
