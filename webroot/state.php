<?

$status = file_get_contents("/tmp/keystate.txt");

print_r($status);


?><div class="verticaldiv"><?

for ($i = 0; $i < 16; $i++) {

	if ($i == 8) { ?></div><div class="verticaldiv"><? }

	if ($status[$i] == "0") {
		$col = "";
	} else {
		$col = "active";
	}
	?>
		<div class="box <?=$col ?>"></div>
	<?
}

?>
</div>