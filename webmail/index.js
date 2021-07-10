function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
  getphp()
} 
function getphp(){
$.get('functions.php', function(data) {
  $("#Getmail .info").html(data);
});
}
function read(){
var dval = $("#Getmail input[name=read]").val();
postp(dval,"read");
}
function del(){
var dval = $("#Getmail input[name=delete]").val();
postp(dval,"del")
}
function send(){
var mailto = $("#mailto").val();
var mailsubj = $("#mailsubj").val();
var mailmsg = $("#mailmsg").val();
var xhr = new XMLHttpRequest();
xhr.open("POST", "post.php", true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify({
    to:   mailto,
    subj: mailsubj,
    msg:  mailmsg
 }));
xhr.onload = function() {
var res = $("#res");
	res.html(this.responseText);
	$("#Sendmail textarea").val("");
}
}
function postp(dval,act){
var v = dval;
var a = act;
var xhr = new XMLHttpRequest();
xhr.open("POST", "action-page.php", true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify({
    dval: v,
     act: a
 }));
xhr.onload = function() {
var res = $("#Getmail .info");
	res.html(this.responseText);
	$("#Getmail input[type=text]").val("");
}
}
