#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides.py
# nwd - największy wspólny dzielnik

def nwd_klasyk(a, b):
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    #print(a)
    
    return a
    
def nww(a, b):
    """
    Oblicza i zwraca najmniejszą wspólną wielokrotność.
    """
    return 0

def main(args):
    a, b = 27, 9
    print("Nwd({}, {}) = {}".format(
                            a,
                            b,
                            nwd_klasyk(a, b))) # wywołanie funkcji
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
