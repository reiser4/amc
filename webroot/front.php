<?

// questa pagina deve leggere il file /var/sr_led.txt in cui saranno memorizzati x byte indicanti l'uscita scritta sullo shift register dei led
// ed accendere i led corrispondenti.


$leds = array(
	"ANT_A_RX_1" => array("x" => 30,"y" => 30,"col" => "red"),
        "ANT_A_RX_2" => array("x" => 30,"y" => 40,"col" => "red"),
        "ANT_A_RX_3" => array("x" => 30,"y" => 50,"col" => "red"),
        "ANT_A_RX_4" => array("x" => 30,"y" => 60,"col" => "red"),
        "ANT_A_RX_5" => array("x" => 30,"y" => 70,"col" => "red"),
        "ANT_A_RX_6" => array("x" => 30,"y" => 80,"col" => "red"),
        "ANT_A_RX_7" => array("x" => 30,"y" => 90,"col" => "red"),
        "ANT_A_RX_8" => array("x" => 30,"y" => 100,"col" => "red"),

        "ANT_A_TX_1" => array("x" => 40,"y" => 30,"col" => "red"),
        "ANT_A_TX_2" => array("x" => 40,"y" => 40,"col" => "red"),
        "ANT_A_TX_3" => array("x" => 40,"y" => 50,"col" => "red"),
        "ANT_A_TX_4" => array("x" => 40,"y" => 60,"col" => "red"),
        "ANT_A_TX_5" => array("x" => 40,"y" => 70,"col" => "red"),
        "ANT_A_TX_6" => array("x" => 40,"y" => 80,"col" => "red"),
        "ANT_A_TX_7" => array("x" => 40,"y" => 90,"col" => "red"),
        "ANT_A_TX_8" => array("x" => 40,"y" => 100,"col" => "red"),

	"ANT_B_RX_1" => array("x" => 90,"y" => 30,"col" => "red"),
        "ANT_B_RX_2" => array("x" => 90,"y" => 40,"col" => "red"),
        "ANT_B_RX_3" => array("x" => 90,"y" => 50,"col" => "red"),
        "ANT_B_RX_4" => array("x" => 90,"y" => 60,"col" => "red"),
        "ANT_B_RX_5" => array("x" => 90,"y" => 70,"col" => "red"),
        "ANT_B_RX_6" => array("x" => 90,"y" => 80,"col" => "red"),
        "ANT_B_RX_7" => array("x" => 90,"y" => 90,"col" => "red"),
        "ANT_B_RX_8" => array("x" => 90,"y" => 100,"col" => "red"),

	"ANT_B_TX_1" => array("x" => 90,"y" => 30,"col" => "red"),
        "ANT_B_TX_2" => array("x" => 90,"y" => 40,"col" => "red"),
        "ANT_B_TX_3" => array("x" => 90,"y" => 50,"col" => "red"),
        "ANT_B_TX_4" => array("x" => 90,"y" => 60,"col" => "red"),
        "ANT_B_TX_5" => array("x" => 90,"y" => 70,"col" => "red"),
        "ANT_B_TX_6" => array("x" => 90,"y" => 80,"col" => "red"),
        "ANT_B_TX_7" => array("x" => 90,"y" => 90,"col" => "red"),
        "ANT_B_TX_8" => array("x" => 90,"y" => 100,"col" => "red"),

);

?>

<div style="position: relative;">

	<? foreach ($leds as $k => $v) { ?>
		<div style="width: 10px; height: 10px; background-color: <?=$v['col'] ?>
		left: <?=$v['x'] ?>; top: <?=$v['y'] ?>; position: absolute;"></div>
	<? } ?>


	<img src="front.jpg" />


</div>
