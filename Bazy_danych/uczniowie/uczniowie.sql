DROP TABLE IF EXISTS uczniowie;
DROP TABLE IF EXISTS klasy;
DROP TABLE IF EXISTS przedmioty;
DROP TABLE IF EXISTS oceny;

CREATE TABLE uczniowie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    plec BOOLEAN,
    id_klasa INTEGER NOT NULL,
    egz_hum NUMERIC NOT NULL DEFAULT 0,
    egz_mat NUMERIC NOT NULL DEFAULT 0,
    egz_jez NUMERIC NOT NULL DEFAULT 0,
    FOREIGN KEY (id_klasa) REFERENCES klasy(id)
    ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE klasy
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    klasa TEXT,
    rok_naboru INTEGER,
    rok_matury INTEGER
);

CREATE TABLE przedmioty
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    przedmiot TEXT,
    imie_naucz TEXT,
    nazwisko_naucz TEXT,
    plec_naucz BOOLEAN
);

CREATE TABLE oceny
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datad DATA,
    id_uczen INTEGER NOT NULL,
    id_przedmiot INTEGER NOT NULL,
    ocena DECIMAL NOT NULL,
    FOREIGN KEY (id_uczen) REFERENCES uczniowie(id)
    FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
);
