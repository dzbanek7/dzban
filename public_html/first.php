<!DOCTYPE html>
<html lang="pl">
<!--
   first.php
-->

<head>
    <meta charset="utf-8" />
    <title>bez nazwy</title>
</head>
<body>

<?php
echo "Witaj!";
// zmienne globalne
$x = 5 * 5;
$txt = "działania";

function myTest() {
    global $x, $txt;
    if ($x > 20)
        echo "<p>Wynik ".$txt.": $x</p>";
}

myTest();

?>

</body>
</html>
