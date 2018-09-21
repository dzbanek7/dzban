#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla_for.py
  

def main(args):
    liczba = int(input('Podaj 1 liczbę: '))
    liczba2 = int(input('Podaj 2 liczbę: '))
    
    while liczba >= liczba2:
        liczba2 = int(input('BŁEDNY ZAKRES! PODAJ NOWY'))
            
    for liczba in range(liczba, liczba2 + 1):
        if liczba % 2 == 0:  
            print(liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
