<?php
$pages = array(
    'wiatam'=>'Aplikacja w PHP',
    'sqlcmd'=>'SQL',
    'formularz'=>'Formularz'
);
function get_menu($id) {
    global $pages;
    foreach ($pages as $klucz => $wartosc) {
        echo 
        '<li class="nav-item">
            <a class="nav-link js-scroll-trigger" href="?id='.$klucz.'">'.$wartosc.'</a>
        </li>';
    }
}
?>
