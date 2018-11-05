DROP TABLE IF EXISTS nazwiska;
DROP TABLE IF EXISTS dane_osobowe;
DROP TABLE IF EXISTS oceny;

CREATE TABLE nazwiska
(
	id_ucznia INTEGER PRIMARY KEY,
	Nazwisko TEXT (20),
	Imie1 TEXT (10),
	Imie2 TEXT (10)
);

CREATE TABLE dane_osobowe
(
	id INTEGER,
	Dzien INTEGER,
	Miesiac INTEGER,
	Rok INTEGER,
	M_urodzenia TEXT,
    Wojewodztwo TEXT,
    FOREIGN KEY (id) REFERENCES nazwiska(id_ucznia)
);

CREATE TABLE oceny
(
	id INTEGER,
    zachowanie TEXT(10),
    Rel_ETY VARCHAR,
    Jpol VARCHAR,
    Jang VARCHAR,
    Jniem VARCHAR,
    Mat VARCHAR,
    Hist VARCHAR,
    Geog VARCHAR,
    Biol VARCHAR,
    Fiz VARCHAR,
    Che VARCHAR,
    Tech VARCHAR,
    Info VARCHAR,
    Plas VARCHAR,
    PO VARCHAR,
    WF VARCHAR,
    FOREIGN KEY (id) REFERENCES nazwiska(id_ucznia)
);
