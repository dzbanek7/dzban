#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  model_orm.py

from peewee import *

baza_plik = 'test_orm.db'
######## MODEL
baza = SqliteDatabase(baza_plik)
class BazaModel(Model):
    class Meta:
        database = baza
        
class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egz_hum = DecimalField(default=0) 
    egz_mat = DecimalField(default=0) 
    egz_jez = DecimalField(default=0) 

class Przedmiot(BazaModel):
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = BooleanField()
    
class Ocena(BazaModel):
    data = DateField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='przedmioty')
    ocena = IntegerField(default=0) 
