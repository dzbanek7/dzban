#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza.py
#

import csv
import os.path

def czy_jest(plik):
    '''Funkcja sprawdza czy plik istnieje na dysku '''
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje!".format(plik))
        return False
    return True
            

def dane_z_pliku(nazwa_pliku, separator=','):
    dane = []  # pusta lista na dane
    if not czy_jest(nazwa_pliku):
        return dane 

    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=separator)
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane
    
def dodaj_dane(dane):
    dane = {
        Pytanie: 'pytania',
        Odpowiedzi: 'odpowiedzi'
    }

    for model, plik in dane.items():
        pola = [pole for pole in  model._meta.fields]
        pola.pop(0)
        wpisy = dane_z_pliku(plik + '.csv')
        with baza.atomic():
            model.insert_many(wpisy, fields=pola).execute()
    


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
