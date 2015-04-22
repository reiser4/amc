

<?

                // questa pagina deve leggere il file /tmp/sr_led.txt in cui saranno memorizzati x byte indicanti l'uscita scritta sullo shift register dei led
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
                        "BAND_10" => array("x" => 261, "y" => 31, "col" => "red"),
                        "BAND_12" => array("x" => 275, "y" => 31, "col" => "red"),
                        "BAND_15" => array("x" => 288, "y" => 31, "col" => "red"),
                        "BAND_17" => array("x" => 302, "y" => 31, "col" => "red"),
                        "BAND_20" => array("x" => 315, "y" => 31, "col" => "red"),
                        "BAND_30" => array("x" => 328, "y" => 31, "col" => "red"),
                        "BAND_40" => array("x" => 342, "y" => 31, "col" => "red"),
                        "BAND_60" => array("x" => 355, "y" => 31, "col" => "red"),
                        "BAND_80" => array("x" => 369, "y" => 31, "col" => "red"),
                        "BAND_160" => array("x" => 383, "y" => 31, "col" => "red"),
                        "GROUP_1" => array("x" => 269, "y" => 204, "col" => "red"),
                        "GROUP_2" => array("x" => 282, "y" => 204, "col" => "red"),
                        "GROUP_3" => array("x" => 295, "y" => 204, "col" => "red"),
                        "GROUP_4" => array("x" => 308, "y" => 204, "col" => "red"),
                        "GROUP_5" => array("x" => 322, "y" => 204, "col" => "red"),
                        "GROUP_6" => array("x" => 335, "y" => 204, "col" => "red"),
                        "GROUP_7" => array("x" => 348, "y" => 204, "col" => "red"),
                        "GROUP_8" => array("x" => 362, "y" => 204, "col" => "red"),
                        "NET_B" => array("x" => 503, "y" => 149, "col" => "red"),
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
                	"SPLIT_B_TX" => array("x" => 570, "y" => 177, "col" => "red"),

                );

?>


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
                        foreach ($leds as $k => $v) { 
                                if ($outbin[$pos] == "1") { $show = true; } else { $show = false; }
                                $pos++;
                                if ($show) {
                                ?>
                		<div style="width: 10px; height: 10px; background-color: <?=$v['col'] ?>;
                		left: <?=$v['x'] ?>px; top: <?=$v['y'] ?>px; position: absolute; border-radius: 5px;"></div>
                	<? 
                        }
                        } ?>


                	<img src="front-off.jpg" />


                	<br/>
                	<br/>
                	<center>
                	Relay: <?=file_get_contents("/tmp/relay.txt"); ?>
                	</center>