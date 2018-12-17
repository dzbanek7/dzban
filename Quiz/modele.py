#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py
#  

from peewee import *

baza_plik = 'quiz.db'
baza = SqliteDatabase(baza_plik) #określanie instancji bazy


### MODELE DANYCH ###

class BazaModel(Model):

    class Meta :
        database = baza

class Kategoria(BazaModel): #nazwa classy zawsze z dużej litery

    kategoria = CharField(null=False)
    

class Pytanie(BazaModel):

    pytanie = CharField(null=False)
    kategoria = ForeignKeyField(Kategoria, related_name='pytania')
    

class Odpowiedz(BazaModel):
    
    odpowiedz = CharField(null=False)
    pytanie = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpok = IntegerField(default=0)
