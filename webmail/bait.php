<html>
<head>
<title>webmail</title>
<link rel="stylesheet" type="text/css" href="index.css" />
</head>
<body>
<!-- Tab links -->
<div class="tab">
  <button class="tablinks" onclick="openTab(event, 'Getmail')" id="Getmail_btn">Get Mail</button>
  <button class="tablinks" onclick="openTab(event, 'Sendmail')">Send Mail</button>
</div>
<?php if(!isset($_POST['psw'])){header("location:../index.php");} ?>
<!-- Tab content -->
<div id="Getmail" class="tabcontent">
  <h3>Mail</h3>
<div class="action">
    <input type="text" placeholder="Read x" name="read" size="7">
  	<button class="tablinks" onclick="read()">Init</button>
    <input type="text" placeholder="Delete x-x OR x" name="delete" size="10">
  	<button class="tablinks" onclick="del()">Init</button>
  <div class="info"> &nbsp; </div>
</div>
</div>
<div id="Sendmail" class="tabcontent" style="display: none;">
  <h3>Send Mail</h3>
  <textarea id="mailto" placeholder="To:" rows="1" cols="20"></textarea>
<br>
  <textarea id="mailsubj" placeholder="Subject" rows="1" cols="20"></textarea>
<br>
  <textarea id="mailmsg" placeholder="Message" rows="4" cols="50"></textarea>
<br>
  <button class="tablinks" onclick="send()">Send</button>
<div id="res"></div>
</div>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="index.js"></script>
</div>
</body>
</html>
