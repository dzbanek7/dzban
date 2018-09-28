#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# 
#  pentle_cw_4.py 
# 

def main(args): 

	for liczba in range(10, 100): 
		if liczba % 2 ==0 and liczba % 3 == 0: 
			print (liczba) 
 

if __name__ == '__main__': 
    import sys 
sys.exit(main(sys.argv)) 
