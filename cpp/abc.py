#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunki.py
#program pobiera 3 liczby całkowite i wyświetla liczbe najwiekszą


def maks(args):
    a = int(input('Podaj 1. liczbę: '))
    print(a)
    b = int(input('Podaj 2. liczbę: '))
    print(b)
    c = int(input('Podaj 3. liczbę: '))
    print(c)

    if c <= a >= b:
        print(a, "jest największe")
    elif a <= b >= c:
        print(b, "jest największe")
    else:
        print(c, "jest największe")
    
    return maks

def main(args):
    
    assert(maks(3, 2, 1) == 3)
    assert(maks(2, 3, 1) == 3)
    assert(maks(1, 2, 3) == 3)
    assert(maks(3, 2, 1) == 3)
    assert(maks(3, 2, 1) == 3)
    assert(maks(3, 2, 1) == 3)
    assert(maks(3, 2, 1) == 3)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
