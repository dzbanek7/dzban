<?php
setlocale(LC_ALL, 'pl_PL.UTF-8');
date_default_timezone_set('Europe/Warsaw');
error_reporting(E_ALL);
ini_set('display_errors', 1);
ini_set('log_errors', 1);
ini_set('error_log', 'public_html/kl2ag2/errorlog.txt');

define('DINC', 'inc/');
define('DBASE', 'db/');
chmod(DBASE, 777);
require_once(DINC.'functions.php');

require_once(DBASE.'db.php');
$dbfile=DBASE.'db.sqlite';
$db=null;
$mode=PDO::FETCH_ASSOC;
init_baza($dbfile);
//db_exec($initstr);
require_once(DINC.'user.php');
$user = new user();

$id='witam';
if (isset($_GET['id'])) $id=trim($_GET['id']);

include_once(DINC.'template.php');
print_r($_SESSION);
?>
