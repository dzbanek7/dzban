<?php
    $data1 = 'Adam Słodowy';
    $data2 = 'Adam Slodowy';
    echo hash('md5', $data1);
    echo "\n\r";
    echo hash('sha256', $data2);
    echo "\n\r";
    echo hash('haval256,5', $data2);
?>
