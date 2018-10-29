#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py

import sqlite3


def kwerenda(cur):
    cur. execute("""
        WITH srednie AS (
            SELECT imie, nazwisko, AVG(ocena) AS nota FROM uczniowie
            INNER JOIN oceny ON uczniowie.id = oceny.id_uczen
            GROUP BY uczniowie.id
        ) SELECT nazwisko, imie, nota FROM srednie
          WHERE nota > 3.0 ORDER BY nota DESC LIMIT 5
        
        
    """)
    
    # SELECT * FROM uczniowie WHERE imie = 'Anna' AND nazwisko = 'Ignaczuk'
    # SELECT * FROM uczniowie WHERE nazwisko LIKE 'A%' - drukuje osoby których nazwisko zaczyna się na A-
    # SELECT * FROM uczniowie WHERE imie LIKE '%a' - drukuje osoby których imie kończy się na -a (teorytycznie wszystkie dziewczyny)
    # % - dowolny ciąg znaków, dowolnej długości
    # SELECT COUNT(id) FROM uczniowie WHERE imie LIKE '%a' - zlicza ilośc osób, których imię kończy się na -a 
    # SELECT imie, nazwisko, egz_mat FROM uczniowie WHERE egz_mat > 40 ORDER BY egz_mat DESC - sortuje dane gdzie dane z egz_mat są wyższe od 40 i sortuje po wyniku malejąco
    # SELECT imie, nazwisko, egz_mat FROM uczniowie WHERE egz_mat > 40 ORDER BY nazwisko ASC - sortuje dane gdzie dane z egz_mat są wyższe od 40 i sortuje po nazwisku rosnąco
    # SELECT imie, nazwisko, egz_mat FROM uczniowie WHERE egz_mat > 40 ORDER BY egz_mat DESC LIMIT 5 - sortuje dane gdzie dane z egz_mat są wyższe od 40 i sortuje po wyniku malejąco, ogranicza ilośc rekordów do 5
    # SELECT AVG(egz_mat), AVG(egz_hum), AVG(egz_jez)  FROM uczniowie - kwerenda agregująca, liczy średnią zmienno przecinkową
    # SELECT MAX(egz_mat), MIN(egz_mat) FROM uczniowie
    # SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa = klasy.id - dołacza do tabeli uczniowie tabelę klasy
    # SELECT imie, nazwisko, klasa FROM uczniowie INNER JOIN klasy ON uczniowie.id_klasa = klasy.id WHERE KLASA = "1A" AND rok_naboru = 2012
    #   SELECT imie, nazwisko, klasa FROM uczniowie 
    #   INNER JOIN klasy ON uczniowie.id_klasa = klasy.id 
    #   WHERE klasy.id =(SELECT klasy.id FROM klasy WHERE KLASA = "1A" AND rok_naboru = 2012)
    #       SELECT klasa, AVG(egz_mat) AS sredniaMAT FROM klasy
    #       INNER JOIN uczniowie ON klasy.id = uczniowie.id_klasa 
    #       GROUP BY klasa 
    #       ORDER BY sredniaMAT DESC
    # WITH srednie AS (
    # SELECT imie, nazwisko, AVG(ocena) AS nota FROM uczniowie
    # INNER JOIN oceny ON uczniowie.id = oceny.id_uczen
    # GROUP BY uczniowie.id
    # ) SELECT nazwisko, imie, nota FROM srednie
    # WHERE nota > 3.0 ORDER BY nota DESC LIMIT 5
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)
    

def main(args):
    # KONFIGURACJA #######
    baza_nazwa = 'uczniowie'
    tabele = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    kwerenda(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
