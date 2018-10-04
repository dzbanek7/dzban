#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
# Program drukuje wypełniony prostokąt o bokach podanych przez użytkownia za pomocą podanego znaku

def mai(args):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    c = str(input("Podaj znak drukowania protokąta: "))
    
    i = 0
    j = 0
    
    for i in range(a):
        for j in range(b):
            print(c, end='')
        print()
    
    return 0
    
# Drukowanie pustego protokąta    
    
def main(args):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    c = str(input("Podaj znak drukowania protokąta: "))
    
    i = 0
    j = 0
    
    for i in range(a):
        for j in range(b):
            if 
            if j == 0 or j == b-1:
                print(c, end='')
            else:
                print(c, end='')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
