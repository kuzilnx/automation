<?php
$json = file_get_contents('php://input');
$data = json_decode($json);
foreach ($data as $key => $value) {
	if ( $key == "dval" ){ $dval = $value; }
	if ( $key == "act" ){ $act = $value; }
}
if ($act == "read"){
	$var="s-nail <<EOF";
	$var1="p $dval";
	$var2="EOF";
$myfile = fopen("act.sh", "w") or die("Unable to open file!");
$txt = "#!/bin/bash\n $var\n $var1\n $var2\n $var3";
fwrite($myfile, $txt);
fclose($myfile);
$output=shell_exec("/bin/bash act.sh");
echo "<pre>".$output."</pre>";
}
if ($act == "del"){
	$var="s-nail <<EOF";
	$var1="d $dval";
	$var2="EOF";
$myfile = fopen("act.sh", "w") or die("Unable to open file!");
$txt = "#!/bin/bash\n $var\n $var1\n $var2\n $var3";
fwrite($myfile, $txt);
fclose($myfile);
$output=shell_exec("/bin/bash act.sh");
echo "<pre>".$output."</pre>";
echo "<script>
// On mouse-over, execute myFunction
function myFunction() {
  document.getElementById(\"Getmail_btn\").click(); // Click on the checkbox
}
myFunction();
</script> ";
}
?>
