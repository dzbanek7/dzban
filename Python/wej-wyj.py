#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  szablon.py

def main(args):
    a = str(input('Jak masz na imię?: '))
    b = str(input('Jak masz na nazwisko?: '))
    
    print("Witaj", a,b)
    
    return 0
    
# duck typing

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
