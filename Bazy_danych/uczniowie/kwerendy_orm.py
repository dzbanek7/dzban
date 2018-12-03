#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
from model_orm import *


def kw01():
    # ~query = Uczen.select().order_by(Uczen.nazwisko.asc())
    # ~query = Uczen.select().where(Uczen.imie.startswith('G'))
    # ~query = Uczen.select().where(Uczen.imie.endswith('a'))
    # ~query = Uczen.select().where(Uczen.imie == 'Rafał')
    # ~query = Uczen.select().where(Uczen.egz_mat > 40)
    query = Uczen.select().where(Uczen.egz_mat.between(30, 35))
    for obj in query:
        print(obj.nazwisko, obj.imie, obj.egz_mat)


def kw02():
    query = (Uczen
            .select(Uczen.nazwisko, Uczen.imie, Uczen.klasa.nazwa)
            .join(Klasa)
            .order_by(Uczen.klasa.nazwa.asc())
    )
    for obj in query:
        print(obj.nazwisko, obj.imie, obj.klasa.nazwa)


def main(args):
    baza.connect()
    
    kw02()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
