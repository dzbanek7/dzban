#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)  # losowanie liczby
    # print("Wylosowano: ", liczba)
    # pobieranie danych od użytkownika
    for i in range(3):  # pętla wykunująca poniższe metody 3 razy
        print("Próba", i + 1)
        odp = input("Podaj liczbę od 1 do 10: ")
        print("Podałeś liczbę:", odp)

        if liczba == int(odp):  # porównanie odp z wylosowaną liczbą
            print("Zgadłeś!")
            break  # przerwanie działania pętli
        elif i == 2:
            print("Wylosowano:", liczba)
        else:
            print("Spróbuj innym razem!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
