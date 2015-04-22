<h2>Selezione antenne</h2>
<table style="width: 100%;">
      
<?

$pos = 0;
$code = "\xff\xff\xff\xff\xff\xff\xff\xff"; // servono 57 bits => 8 bytes!
if (file_exists("/tmp/sr_led.txt")) { $code = file_get_contents("/tmp/sr_led.txt"); }
$outbin = "";
for ($i = 0; $i < strlen($code); $i++) {
        $char = $code[$i];
        $bin = str_pad(decbin(ord($char)),8,"0",STR_PAD_LEFT);
        $outbin .= $bin;
        //echo "/".$bin . "\\";
}
//echo $outbin;
//echo strlen($outbin);
$rxA = -1;
$rxB = -1;
$txA = -1;
$txB = -1;
for ($i = 0; $i < strlen($outbin); $i++) {
        if ($i >= 0 && $i < 8) {
                if ($outbin[$i] == "1") {
                        $rxA = $i - 0;
                }
        }
        if ($i >= 9 && $i < 9+8) {
                if ($outbin[$i] == "1") {
                        $txA = $i - 9;
                }
        }
        if ($i >= 39 && $i < 39+8) {
                if ($outbin[$i] == "1") {
                        $rxB = $i - 39;
                }
        }
        if ($i >= 48 && $i < 48+9) {
                if ($outbin[$i] == "1") {
                        $txB = $i - 48;
                }
        }
} 


?>

  <tr>
        <td rowspan="9"><h2>A</h2></td>
        <td>RX: <?=$rxA+1 ?></td> 
        <td>TX: <?=$txA+1 ?></td>
        <td>Antenna</td>
        <td>RX: <?=$rxB+1 ?></td>
        <td>TX: <?=$txB+1 ?></td>
        <td rowspan="9"><h2>B</h2></td>
        </tr>

<?

$antenne = array("Optibeam","Tribander","Dip. 40", "80+160", "80 Wideband","Dummy l.","","");
$c= 1;
foreach ($antenne as $a) {
?>
        <tr>
        <td><a <? if ($rxA+1 == $c) { echo "class='active'"; } ?> 
                href="javascript:antennaRequest('A', 'rx', '<?=$c ?>');"><?=$c ?></a></td>
        <td><a <? if ($txA+1 == $c) { echo "class='active'"; } ?> 
                href="javascript:antennaRequest('A', 'tx', '<?=$c ?>');"><?=$c ?></a></td>
        <td><?=$a ?></td>
        <td><a <? if ($rxB+1 == $c) { echo "class='active'"; } ?> 
                href="javascript:antennaRequest('B', 'rx', '<?=$c ?>');"><?=$c ?></a></td>
        <td><a <? if ($txB+1 == $c) { echo "class='active'"; } ?> 
                href="javascript:antennaRequest('B', 'tx', '<?=$c ?>');"><?=$c ?></a></td>
        </tr>
<? $c++; } ?>




</table>