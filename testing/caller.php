<?php
    $item='Scott_Embleau,3,,Earl_Swindle,17,,Richard_Myrick,8,,Steve_Crane,7,,Bob_Mitzel,7,,Michael_Price,14,,Robert_Jansen,2,,Paul_Hollenstein,10,,Ken_Brosnahan,15,,Timothy_Vola,3,,John_Foster,6,,Tommy_Zielinski,8,,Kurt_Thomson,14,,Mick_Migdall,14,,Jeff_Unger,16,,Marc_Timson,9,,';
    $tmp = exec("python groups.py $item");
    echo $tmp;
?>
