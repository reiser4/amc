<?

// questa pagina deve leggere il file /var/sr_led.txt in cui saranno memorizzati x byte indicanti l'uscita scritta sullo shift register dei led
// ed accendere i led corrispondenti.


$leds = array(
	"ANT_A_RX_1" => array("x" => 61,"y" => 62,"col" => "red"),
        "ANT_A_RX_2" => array("x" => 61,"y" => 75,"col" => "red"),
        "ANT_A_RX_3" => array("x" => 61,"y" => 88,"col" => "red"),
        "ANT_A_RX_4" => array("x" => 61,"y" => 102,"col" => "red"),
        "ANT_A_RX_5" => array("x" => 61,"y" => 116,"col" => "red"),
        "ANT_A_RX_6" => array("x" => 61,"y" => 129,"col" => "red"),
        "ANT_A_RX_7" => array("x" => 61,"y" => 143,"col" => "red"),
        "ANT_A_RX_8" => array("x" => 61,"y" => 156,"col" => "red"),

	"SPLIT_A_RX" => array("x" => 61,"y" => 177,"col" => "red"),

        "ANT_A_TX_1" => array("x" => 82,"y" => 62,"col" => "red"),
        "ANT_A_TX_2" => array("x" => 82,"y" => 75,"col" => "red"),
        "ANT_A_TX_3" => array("x" => 82,"y" => 88,"col" => "red"),
        "ANT_A_TX_4" => array("x" => 82,"y" => 102,"col" => "red"),
        "ANT_A_TX_5" => array("x" => 82,"y" => 116,"col" => "red"),
        "ANT_A_TX_6" => array("x" => 82,"y" => 129,"col" => "red"),
        "ANT_A_TX_7" => array("x" => 82,"y" => 143,"col" => "red"),
        "ANT_A_TX_8" => array("x" => 82,"y" => 156,"col" => "red"),

	"SPLIT_A_TX" => array("x" => 82, "y" => 177, "col" => "red"),

	"NET_A" => array("x" => 165, "y" => 149, "col" => "red"),

	"BAND_6" => array("x" => 248, "y" => 31, "col" => "red"),

	"ANT_B_RX_1" => array("x" => 549,"y" => 62,"col" => "red"),
        "ANT_B_RX_2" => array("x" => 549,"y" => 75,"col" => "red"),
        "ANT_B_RX_3" => array("x" => 549,"y" => 88,"col" => "red"),
        "ANT_B_RX_4" => array("x" => 549,"y" => 102,"col" => "red"),
        "ANT_B_RX_5" => array("x" => 549,"y" => 116,"col" => "red"),
        "ANT_B_RX_6" => array("x" => 549,"y" => 129,"col" => "red"),
        "ANT_B_RX_7" => array("x" => 549,"y" => 143,"col" => "red"),
        "ANT_B_RX_8" => array("x" => 549,"y" => 156,"col" => "red"),

	"SPLIT_B_RX" => array("x" => 549,"y" => 177, "col" => "red"),

	"ANT_B_TX_1" => array("x" => 570,"y" => 62,"col" => "red"),
        "ANT_B_TX_2" => array("x" => 570,"y" => 75,"col" => "red"),
        "ANT_B_TX_3" => array("x" => 570,"y" => 88,"col" => "red"),
        "ANT_B_TX_4" => array("x" => 570,"y" => 102,"col" => "red"),
        "ANT_B_TX_5" => array("x" => 570,"y" => 116,"col" => "red"),
        "ANT_B_TX_6" => array("x" => 570,"y" => 129,"col" => "red"),
        "ANT_B_TX_7" => array("x" => 570,"y" => 143,"col" => "red"),
        "ANT_B_TX_8" => array("x" => 570,"y" => 156,"col" => "red"),

	"SPLIT_B_TX" => array("x" => 570, "y" => 177, "col" => red),

);

?>

<div style="position: relative;">

	<? foreach ($leds as $k => $v) { ?>
		<div style="width: 10px; height: 10px; background-color: <?=$v['col'] ?>;
		left: <?=$v['x'] ?>px; top: <?=$v['y'] ?>px; position: absolute; border-radius: 5px;"></div>
	<? } ?>


	<img src="front.jpg" />


</div>
