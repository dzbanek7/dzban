#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfry.py

def sumuj_cyfry1(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10 
        liczba = int(liczba / 10)
    return suma


def main(args):
    
    liczba = int(input("Podaj dowolną liczbę dwucyfrową: "))
    
    while liczba < 10:
        liczba = int(input("Podaj dowolną liczbę dwucyfrową: "))
    
    print("Suma cyfr : ", sumuj_cyfry1(liczba))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
