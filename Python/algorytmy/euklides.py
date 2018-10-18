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
<<<<<<< HEAD:algorytmy/euklides.py
    nww = 0
=======
    
>>>>>>> f28febc688eca5ea009b3b4533b2887d76ff2e84:Python/algorytmy/euklides.py
    nww = a * b / nwd_klasyk(a, b)
    
    return nww

def main(args):
<<<<<<< HEAD:algorytmy/euklides.py
    a = int(input('Podaj 1 liczbę: '))
    b = int(input('Podaj 2 liczbę: '))
=======
    a = int(input("Podaj pierwsza liczbe: "))
    b = int(input("Podaj drugą liczbe: "))
>>>>>>> f28febc688eca5ea009b3b4533b2887d76ff2e84:Python/algorytmy/euklides.py
    print("Nwd({}, {}) = {}".format(
                            a,
                            b,
                            nwd_klasyk(a, b))) # wywołanie funkcji
    print("Nww({}, {}) = {}".format(
                            a,
                            b,
                            nww(a, b))) # wywołanie funkcji
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
