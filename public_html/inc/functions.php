<?php
$kom = []; // tablica komunikatów
$pages = array(
    'witam'=>'Aplikacja w PHP',
    'sqlcmd'=>'SQL',
    'formularz'=>'Formularz'
);
function get_page_title($id) {
    global $pages;
    if (array_key_exists($id, $pages))
        echo $pages[$id];
    else 
        echo 'Aplikacja w PHP';
}

function get_kom(){
    global $kom;
    foreach ($kom as $k)
        echo '<p class="lead">'.$k.'</p>';
}

function get_page_content($id) {
    global $pages, $kom;
    if (file_exists($id.'.html'))
        include($id.'html');
    else
        $kom[]='Brak strony: '.$id;
}


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
