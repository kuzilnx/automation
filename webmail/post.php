<?php
$json = file_get_contents('php://input');
$data = json_decode($json);
foreach ($data as $key => $value) {
	if ( $key == "to" ){ $to = $value; }
	if ( $key == "subj" ){ $subj = $value; }
	if ( $key == "msg" ){ $msg = $value; }
}
$var="echo $msg | s-nail -s '$subj' $to > msg 2>&1";
exec($var);
?>
