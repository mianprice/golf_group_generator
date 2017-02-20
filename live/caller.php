<?php
    $item1='123456,3:987654,17:3456,8:9876,7:4567,7:987643,14:23457857,2:0327403270,10:81739179,15:2163812763,3:8312963,6:028193710,8:382179,14:381721987,14:32890179,16:3278917,9';
    $item2='Person_A,5:Person_B,3:Person_C,7:Person_D,9:Person_E,16:Person_F,13:Person_G,12:Person_H,15:Person_I,9:Person_J,14:Person_K,13:Person_L,18';
    $tmp = exec("python groups.py $item1");
    echo $tmp;
?>
