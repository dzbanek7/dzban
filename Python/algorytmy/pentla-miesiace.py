#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pentla-miesiace.py
#  

def main(args):
	nazwy = ['styczeń','luty','marzec','kwieceń','maj','czerwiec','lipiec','sierpień','wrzesień','październik','listopad','grudzień']
	
	while 1 > 0:
		numer = int(input("Podaj numer miesiąca: "))
		if 1 > numer > 12:
			print("Wprowadzone dane są błędne! ")
		else:
			print (nazwy[numer - 1])
	return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
