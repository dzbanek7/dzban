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
    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])
    
    kl1 = Klasa(nazwa='2A', roknaboru=2012, rokmatury=2015)
    kl1.save()
    kl2b = Klasa(nazwa='2B', roknaboru=2012, rokmatury=2015)
    kl2b.save()
    kl3a = Klasa(nazwa='3A', roknaboru=2011, rokmatury=2014)
    kl3a.save()
    
    kl2a = Klasa.select().where(Klasa.nazwa=='2A').get()
    u1 = Uczen(imie='Stanisław', nazwisko='Koniecpolski', plec=False, klasa=kl2a)
    u1.save()
    u2 = Uczen(imie='Klemens', nazwisko='Branicki', plec=False, klasa=kl2b)
    u2.save()
    u3 = Uczen(imie='Izabela', nazwisko='Czartoryska', plec=True, klasa=kl3a)
    u3.save()
    
    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.imie, uczen.nazwisko)
    uczniowie
    
    
    klasa = Klasa.select()
    for klasa in Klasa:
        print(klasa.id, klasa.nazwa, klasa.roknaboru, klasa.rokmatury)
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
