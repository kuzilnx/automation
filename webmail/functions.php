<?php
$output=null;
$retval=null;
exec('s-nail', $output, $retval);
foreach ($output as $key => $value) {
	if ( $key != 1 ){
		echo $value."<br/>";
	}
}
?>
