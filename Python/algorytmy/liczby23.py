#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py

def liczby2():
    """
    Funkcja drukuje wszystkie liczby 2-cyfrowe, w których cyfry nie powtarzają się. Funkcja zwraca ich liczbę.
    Wykluczone liczby: 11, 22, 33 itd.
    """
    
    ile = 0
    
    for i in range(1, 10):
        for j in range(0, 10):
            if i == j:
                print("", end = '')
            else:
                print("{}{} ".format(i,j), end='')
                ile = ile + 1
    
    return ile
    
def liczby3():
    """
    Funkcja drukuje wszystkie liczby 3-cyfrowe, w których cyfry nie powtarzają się. Funkcja zwraca ich liczbę.
    Wykluczone liczby: 111, 222, 333, 110, 211 itd.
    """
    
    ile = 0 # licznik
    
    for i in range(1, 10): # cyfra setek
        for j in range(0, 10): # cyfra dziesiątek
            for k in range(0, 10): # cyfra jedności
                if i == j or i == k or k == j:
                    print("", end = '')
                else:
                    print("{}{}{} ".format(i,j,k), end='')
                    ile = ile + 1
    
    return ile

def main(args):
    print("Liczby 2-cyfrowych: ", liczby2())
    print("Liczby 3-cyfrowych: ", liczby3())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
