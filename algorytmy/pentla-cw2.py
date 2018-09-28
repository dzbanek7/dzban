#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-cw1.py
#  


def main(args):
    a = int(input("Podaj liczbę początkową zakresu: "))
    b = int(input("Podaj liczbę końcową zakresu: "))
    

    for liczba in range(a, b + 1):
        print(liczba, end = " ")  
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
