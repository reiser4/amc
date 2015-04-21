<?

$status = file_get_contents("/tmp/keystate.txt");

print_r($status);


?><div class="verticaldiv"><?

foreach ($i = 0; $i < strlen($status); $i++) {

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