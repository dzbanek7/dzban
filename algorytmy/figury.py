#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py
# Program drukuje wypełniony prostokąt o bokach podanych przez użytkownia za pomocą podanego znaku

def prostokat(a, b, c):
    
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
    
def prostokat2(a, b, c):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    c = str(input("Podaj znak drukowania protokąta: "))
    
    i = 0
    j = 0
    
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b-1 or i == 0 or i == a - 1:
                print(c, end='')
            else:
                print(" ", end='')
        print()
    
    return 0
    
def choinka(h, znak):
    
    h = int(input("Podaj wysokośc choinki: "))
    znak = str(input("Podaj znak drukowania choinki: "))
    
    for i in range(h):
        for j in range(i + 1):
            print(znak, end = '')
        print()
    
    return 0

def choinka2(h, znak):
    
    h = int(input("Podaj wysokośc choinki: "))
    znak = str(input("Podaj znak drukowania choinki: "))
    
    for i in range(h):
        for j in range(h - i):
            print(znak , end = '')
        print()
    
    return 0
    
def trujkat(h, znak):
    
    h = int(input("Podaj wysokośc choinki: "))
    znak = str(input("Podaj znak drukowania choinki: "))
    
    for i in range(h):
        for j in range(h + i):
            print(znak , end = '')
        print()
    
    return 0

def main(args):
    h, znak = 6, "$"
    choinka2(h, znak)
    print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
