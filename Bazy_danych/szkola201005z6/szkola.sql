DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS oceny;

CREATE TABLE przedmioty
(
	IDprzedmiotu INTEGER PRIMARY KEY,
	NazwaPrzedmiotu TEXT (20),
	Nazwisko_naucz TEXT (20),
	Imie_naucz TEXT (10)
);

CREATE TABLE uczniowie
(
	IDucznia INTEGER PRIMARY KEY,
	nazwisko TEXT,
    imie TEXT,
    ulica TEXT,
    dom INTEGER,
    IDklasy TEXT
);

CREATE TABLE oceny
(
	IDucznia INTEGER,
    Ocena VARCHAR,
    Data_ DATA, 
    IDprzedmiotu INTEGER,
    FOREIGN KEY (IDucznia) REFERENCES uczniowie(IDucznia),
    FOREIGN KEY (IDprzedmiotu) REFERENCES przedmioty(IDprzedmiotu)
);

