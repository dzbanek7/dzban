DROP TABLE IF EXISTS tbUczniowie;
CREATE TABLE tbUczniowie (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT,
	nazwisko TEXT,
	plec INTEGER,
	id_Klasa INTEGER NOT NULL REFERENCES tbklasy(id),
	egzHum NUMERIC NOT NULL DEFAULT 0,
	egzMat NUMERIC NOT NULL DEFAULT 0,
	egzJez NUMERIC NOT NULL DEFAULT 0
	);

DROP TABLE IF EXISTS tbKlasy;
CREATE TABLE tbKlasy (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
	klasa TEXT,
	rokNaboru INTEGER,
	rokMatury INTEGER
);

DROP TABLE IF EXISTS tbPrzedmioty;
CREATE TABLE tbPrzedmioty (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
	przedmiot TEXT,
	nazwiskoNaucz TEXT,
	imieNaucz TEXT,
	plecNaucz INTEGER
);

DROP TABLE IF EXISTS tbOceny;
CREATE TABLE tbOceny (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
	ocena NUMERIC,
	datad DATE,
	idUczen INTEGER NOT NULL REFERENCES tbUczniowie(id),
	idPrzedmiot INTEGER NOT NULL REFERENCES tbPrzedmioty(id)

);

INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1B', 2015, 2018);
INSERT INTO tbKlasy VALUES (NULL, '1A', 2015, 2018);

INSERT INTO tbUczniowie(id, imie, nazwisko, plec, id_Klasa, egzHum, egzMat, egzJez)
VALUES (NULL, 'Adam', 'Kowalski', 0, 1, 80.6, 50, 90.5);
INSERT INTO tbUczniowie VALUES (NULL, 'Ilona', 'Nowak', 1, 2, 50.6, 78.9, 80);
INSERT INTO tbUczniowie VALUES (NULL, 'Jaś', 'Fasola', 0, 2, 70.7, 67.7, 90);

INSERT INTO tbPrzedmioty(id, przedmiot, nazwiskoNaucz, imieNaucz, plecNaucz) VALUES (NULL, 'Biologia','Henryszewski', 2018);

