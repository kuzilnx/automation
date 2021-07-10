<?php
// define variables and set to empty values
$psw = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $psw = test_input($_POST["psw"]);
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
echo "<br>";
if ($psw == "2347"){
	include("bait.php");
}
?>
