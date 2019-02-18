<!DOCTYPE html>
<html lang="pl">
<!--
   first.php
-->

<head>
<meta charset="utf-8" />
<title>bez nazwy</title>
<meta name="generator" content="Geany 1.32" />
</head>

<body>
    
<?php
echo "Witaj!";
// zmienne globalne
$x = 5 * 5; // zmienną dekalurejmy zawsze przez $. np. $x 
$txt = "działania";

// php tak jak python nie wymaga deklarowania typu danych jak w cpp (int, string)
function myTest() {
    global $x;
    global $txt;
    if ($x > 20)
        echo "<p>Wynik ".$txt.": $x</p>"; // jest różnica pomiedzy '', a "" bo za pomocą '' dostaniemy tylko tekst, za "" kod php     
}

// zmienną tekstową $txt w tekście deklarujemy przez ".$txt." 
// w funkcjach trzeba deklarować zmienne globalne ponownie
myTest();

?>

</body>

</html>
