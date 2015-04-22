<?

$status = file_get_contents("/tmp/keystate.txt");

print_r($status);

$antenne = array("Optibeam","Yagi 3 el", "Dip. 40", "Dip. 80+160", "Dip. 80 CW+SSB","Dummy","","");

?><br/>

<table>
<tr>
	<td rowspan="9">Radio A</td>
	<td></td>
	<td align="center">Antenna</td>
	<td></td>
	<td rowspan="9">Radio B</td>
	</tr>
	<?
$counttxA = 0;
$countrxA = 0;
$counttxB = 0;
$countrxB = 0;
$txA = -1;
$txB = -1;
$rxA = -1;
$rxB = -1;
for ($i = 0; $i < 8; $i++) {

	if ($status[$i] == "0") {
		$colA = "";
	} else if ($status[$i] == "2") {
		$counttxA++;
		$colA = "tx";
		$txA = $i;
		if ($rxA == -1) { $rxA = $i; }
	} else {
		$countrxA++;
		$colA = "active";
		$rxA = $i;
	}
	if ($status[$i+8] == "0") {
		$colB = "";
	} else if ($status[$i+8] == "2") {
		$counttxB++;
		$colB = "tx";
		$txB = $i+8;
		if ($rxB == -1 && $rxA != $i) { $rxB = $i+8; }
	} else {
		$countrxB++;
		$colB = "active";
		if ($rxA != $i) { $rxB = $i+8; }
	}
	
	?>  <tr>
		<td align="center" class="pin <?=$colA ?>"><?=$i ?></td>
		<td align="center"><?=$antenne[$i] ?></td>
		<td align="center" class="pin <?=$colB ?>"><?=$i+8 ?></td>
		</tr>
	<?
}

?>
</tr>
</table>

<div>
	Errori riscontrati:<br/><span style="color: darkRed">
	<?

if ($counttxA == 0) { echo "Trasmissione non attivata per A<br/>"; }
if ($counttxB == 0) { echo "Trasmissione non attivata per B<br/>"; }
if ($counttxA > 1) { echo "Due o piu` ant. di trasmissione per A<br/>"; }
if ($counttxB > 1) { echo "Due o piu` ant. di trasmissione per B<br/>"; }
if ($countrxA > 1) { echo "Due o piu` ant. di ricezione per A<br/>"; }
if ($countrxB > 1) { echo "Due o piu` ant. di ricezione per B<br/>"; }
if ($rxA == $rxB) { echo "Conflitto sulle antenne di ricezione<br/>"; }

	?></span>
</div>
<div>
Setup finale:<br/>
Stazione A: Tx su <?=$txA ?>; Rx su <?=$rxA ?><br/>
Stazione B: Tx su <?=$txB ?>; Rx su <?=$rxB ?><br/>
