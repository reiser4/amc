<?


$radio = $_GET['radio'];
$ant = $_GET['ant'];
$type = $_GET['type'];


$outfile = "/tmp/radio" . $radio . $type . ".txt";

$outstring = "00000000";
$outstring[$ant-1] = "1";

$outint = bindec($outstring);
$outchar = chr($outint);

file_put_contents($outfile, $outchar);

header("Location: front.php");