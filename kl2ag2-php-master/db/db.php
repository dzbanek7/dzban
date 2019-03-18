<?php
function init_baza($dbfile) {
	global $db,$kom;
	try {
		if (!file_exists($dbfile)) $kom[]='Próba utworzenia nowej bazy...';
		$db=new PDO("sqlite:$dbfile");
		$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	} catch(PDOException $e) {
		echo ($e->getMessage());
	}
}

function db_exec($qstr) {
	global $db,$kom;
	$kom[]='Wykonuję: '.$qstr.'<br />';
	$ret=null;
	try {
		$ret=$db->exec($qstr);
	} catch(PDOException $e) {
		echo ($e->getMessage());
	}
	return $ret;
}

function db_lastInsertID() {
	global $db;
	return $db->lastInsertId();
}

function get_err() {
	global $db,$kom;
	foreach ($db->errorInfo() as $e)
		if ($e!='00000') $kom[]=$e;
}

function db_query($qstr,&$ret=null) {
	global $db,$mode,$mode;
	$kom[]='Wykonuję: '.$qstr.'<br />';
	$res=null;
	try {
		$res=$db->query($qstr);
	} catch(PDOException $e) {
		echo ($e->getMessage());
	}
	if ($res) $ret=$res->fetchAll($mode);
	if (empty($ret)) return false;
	return true;
	}

$initstr="BEGIN;
CREATE TABLE users (
    uid INTEGER PRIMARY KEY NOT NULL,
    login CHAR(20) UNIQUE NOT NULL,
    haslo CHAR(50) NOT NULL,
    email CHAR(40) UNIQUE NOT NULL,
    datad INT NOT NULL
);
INSERT INTO users VALUES (NULL, 'admin', '".sha1('haslo')."', 'admin@home.net', ".time().");
COMMIT;
CREATE TABLE uczniowie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    plec BOOLEAN,
    id_klasa INTEGER NOT NULL,
    FOREIGN KEY (id_klasa) REFERENCES klasy (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
);
CREATE TABLE klasy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    klasa TEXT(2),
    rok_naboru INTEGER,
    rok_matury INTEGER
);
";

?>
