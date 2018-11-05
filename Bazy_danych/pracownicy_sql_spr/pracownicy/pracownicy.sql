DROP TABLE IF EXISTS kontakty;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS pracownicy;
DROP TABLE IF EXISTS stanowiska;

CREATE TABLE kontakty
(
	id_pracownika INTEGER,
	typ_k INTEGER,
	kontakt TEXT (15),
	uwagi TEXT (15),
    FOREIGN KEY (id_pracownika) REFERENCES pracownicy(id)
);

CREATE TABLE place
(
	id_p INTEGER,
    id_s INTEGER,
    placa DECIMAL,
    data_z data,
    FOREIGN KEY (id_p) REFERENCES pracownicy(id),
    FOREIGN KEY (id_s) REFERENCES stanowiska(id)
);

CREATE TABLE pracownicy
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT(20), 
    nazwisko TEXT(20), 
    kod TEXT(10), 
    miasto_z TEXT(20), 
    ulica TEXT(20), 
    data_u DATA, 
    miasto_u TEXT(20)
);

CREATE TABLE stanowiska
(
    id_s INTEGER PRIMARY KEY AUTOINCREMENT,
	stanowisko TEXT(20)
);

