#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
#  

def main(args):
	
	liczba = int(input("Podaj liczbę: "))
	
	cyfry = list(map(int, str(liczba)))

	print ("Suma cyfr liczby:", sum(cyfry))

	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
