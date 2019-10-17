CREATE TABLE uczniowie (
	id_ucz CHAR(8) PRIMARY KEY,
	imie VARCHAR(30) NOT NULL,
	nazwisko VARCHAR(30) NOT NULL,
	id_klasa INTEGER DEFAULT ''
);

CREATE TABLE oceny (
	id_oceny INTEGER PRIMARY KEY AUTOINCREMENT,
	data DATE,
	id_ucz CHAR(8) NOT NULL ,
	id_przedm INTEGER,
	ocena DECIMAL(3,2),
	FOREIGN KEY (id_ucz) REFERENCES uczniowie(id_ucz)
);

CREATE TABLE klasy (
	id_klasa INTEGER,
	klasa CHAR(4)
);

-- tabela słownikowa
CREATE TABLE przedmioty (
	id_przedm INTEGER,
	nazwa VARCHAR(30)
);