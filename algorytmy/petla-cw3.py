#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla-cw3.py

def main(args):
	a = int(input("Podaj liczbę końcową zakresu: "))
    
    for liczba in range(0, a + 1):
        print(liczba * liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
