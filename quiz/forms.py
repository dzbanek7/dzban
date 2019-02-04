#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  forms.py

from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, BooleanField
from wtforms import SelectField, FormField, FieldList
from wtforms.validators import Required


blad1='To pole jest wymagane!'

class OdpForm(FlaskForm):
    id = HiddenField()
    pytanie = HiddenField()
    odpowiedz = StringField('Odpowiedź:', validators=[Required(message=blad1)])
    odpok = BooleanField('Poprawna:')

class DodajForm(FlaskForm):
    id = HiddenField()
    pytanie = StringField('Treść pytania:', validators=[Required(message=blad1)])
    kategoria = SelectField('Kategoria', coerce=int)
    odpowiedzi = FieldList(FormField(OdpForm), min_entries=3)

