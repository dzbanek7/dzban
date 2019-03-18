<?php
ini_set('session.use_cookies', 1);
ini_set('session.use_only_cookies', 1);
ini_set('session.save_path', 'sesje');
ini_set('session.gc_probability', 1);
ini_set('session.cookie_httponly', 1);

class user {
	var $uVal = 'uval';
	var $remTime = 7200; // 2 godz.
	var $remCookieDomain = '';
	var $remCookieName = 'sqlDB';
	var $keys = array('uid', 'login', 'haslo', 'email', 'datad');
	var $dane = array();
	var $kom = array();

	function __construct() {
		$this->remCookieDomain = ($this->remCookieDomain == '' ? $_SERVER['HTTP_HOST'] : $this->remCookieDomain);
		if(!isset($_SESSION)) session_start();
		if(!empty($_SESSION[$this->uVal])) $this->is_user($_SESSION[$this->uVal]);
		if (isset($_COOKIE[$this->remCookieName]) && !$this->uid) {
			$u = unserialize(base64_decode($_COOKIE[$this->remCookieName]));
			$this->login($u['login'],$u['haslo'],false,true);
		}
		if (!$this->uid && isset($_POST['loguj'])) {
			$n = clrtxt($_POST['login']); //nazwa użytkownika
			$h = clrtxt($_POST['haslo']); //hasło użytkownika
			$this->login($n,$h,true,true);
		}
		if (isset($_GET['unlog'])) $this->logout();
	}

	function is_user($sid, $login=NULL, $haslo=NULL) {
		if (!empty($login)) {
			$qstr='SELECT * FROM users WHERE login=\''.$login.'\' AND haslo = \''.sha1($haslo).'\' LIMIT 1';
		} else return false;

		$ret = array();
		db_query($qstr, $ret);
		if (!empty($ret[0])) {
			$this->dane=array_merge($this->dane, $ret[0]);
			$sid = sha1($this->uid.$this->login.session_id());
			$_SESSION[$this->uVal] = $sid;
			return true;
		}
	}

	function login($login, $haslo, $remember=false, $loadUser=true) {
		$login = rescape($login);
		$haslo = rescape($haslo);
		if ($loadUser && $this->is_user('',$login,$haslo)) {
			if ($remember) { // zapisanie ciasteczka
			  $cookie = base64_encode(serialize(array('login'=>$login,'haslo'=>$haslo,'czas'=>time())));
			  $a = setcookie($this->remCookieName,$cookie,time()+$this->remTime,'/',$this->remCookieDomain,false,true);
			}
			$this->kom[]='Witaj '.$login.'! Zostałeś zalogowany.';
			return true;
		}
		$this->kom[]='<b>Błędny login lub hasło!</b>';
		return false;
	}

	function logout($redirectTo = '') {
		//if (isset($_SESSION[$this->uVal])) {
		//	if (!db_exec('UPDATE uinfo SET sid = \'\' WHERE sid = \''.$_SESSION[$this->uVal].'\'')) $this->kom[]='Błąd sesji.';
		//}
		setcookie($this->remCookieName,'', time()-($this->remTime*3),'/',$this->remCookieDomain,false,true);
		$this->dane=array();
		$_SESSION = array();
		if (ini_get("session.use_cookies")) {
    		$params = session_get_cookie_params();
    		setcookie(session_name(),'',time()-($this->remTime*3),$params["path"], $params["domain"],$params["secure"],$params["httponly"]);
		}
		if (session_destroy()) $this->kom[]='Zostałeś wylogowany.';
		if ($redirectTo != '' && !headers_sent()) {//ewentualne przekierowanie
			header('Location: '.$redirectTo);
			exit;//To ensure security
		}
 }

	function savtb() {//tab. asocjacyjna z kluczami: uid#login#haslo#email#datad
		if (strlen($this->haslo)<40) $this->haslo=sha1($this->haslo);
		$this->llog=time();
		if (!$this->uid) {
			$qstr='INSERT INTO users VALUES (NULL,\''.$this->login.'\',\''.$this->haslo.'\',\''.$this->email.'\',time())';
			$ret=db_exec($qstr);
			$uid = db_lastInsertID();
			// if ($ret && $uid) {
			// 	$qstr='INSERT INTO uinfo (uid) VALUES ('.$uid.')';
			// 	$ret=db_exec($qstr);
			// } else $this->kom[]='Błąd zapisu podstawowych danych użytkownika.';
		}
		if ($ret) return true;
		return false;
	}

	function __set($k, $v) {
	  $this->dane[$k] = $v;
	}

	function __get($k) {
		if (array_key_exists($k, $this->dane))
			return $this->dane[$k];
		return null;
	}

	function getKom() {
		foreach ($this->kom as $kom) echo '<p class="text-info">'.$kom.'</p>';
		$this->kom = array();
	}

	function is_login($login) {
		$qstr = 'SELECT uid FROM users WHERE login=\''.$login.'\' LIMIT 1';
    if (db_query($qstr)) return true;
    return false;
	}

	function is_email($email) {
		$qstr = 'SELECT uid FROM users WHERE email=\''.$email.'\' LIMIT 1';
    if (db_query($qstr)) return true;
    return false;
	}

}
?>