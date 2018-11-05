#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py
import os
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
    
class Wynik(BazaModel):
    egz_hum = DecimalField(default=0) 
    egz_mat = DecimalField(default=0) 
    egz_jez = DecimalField(default=0) 
    klasa = ForeignKeyField(Uczen, related_name='wyniki')
    
def main(args):

    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
