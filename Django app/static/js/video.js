
function loadfunc(){
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    var resp = this.responseText;
    if(resp=="ON"){
    document.getElementById("tools").disabled=false;
    document.getElementById("switch-point").style.marginLeft="65%";
    document.getElementById("switch-point").style.backgroundColor="white";
    document.getElementById("switch").style.backgroundColor="blue";
    document.getElementById("switch").style.borderColor = "blue";
    document.getElementById("status").innerHTML="On";
    document.getElementById("camoff").style.display="none";
    document.getElementById("loading").style.display="none";
    document.getElementById("vid").style.display="block";
    document.getElementById("control").src='https://toplofty-rat-9906.dataplicity.io/control.htm';
    document.getElementById("notifications").innerHTML ="<li>"+"camera is on"+"</li>";
    }
    else{
    document.getElementById("vid").src='';
    }
    }
  };
  xhttp.open("get", "/camera_status", true);
  xhttp.send();
 }
loadfunc();

function mDown(obj) {
var m=document.getElementById("switch-point").style.marginLeft;
  obj.style.backgroundColor = "grey";
  obj.style.borderColor = "grey";
  document.getElementById("switch-point").style.backgroundColor="white";
}

function mUp() {
var obj=document.getElementById("switch");
var m=document.getElementById("switch-point").style.marginLeft;
if(m!="65%"){
  obj.style.backgroundColor="blue";
  obj.style.borderColor = "blue";
  var i=8;
  for(i=8;i<=65;i++)
  {
  document.getElementById("switch-point").style.marginLeft=i+"%";
  }
  document.getElementById("status").innerHTML="On";
  document.getElementById("camoff").style.display="none";
  document.getElementById("loading").style.display="block";

  var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    var nt=document.getElementById("notifications").innerHTML;
    document.getElementById("notifications").innerHTML ="<li>"+ this.responseText + "</li>"+nt;
    }
  };
  xhttp.open("GET", "/change_camera", true);
  xhttp.send();

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
  var resp = this.responseText;
  if(resp=="done"){
  document.getElementById("loading").style.display="none";
  document.getElementById("camoff").style.display="none";
  document.getElementById("vid").style.display="block";
  document.getElementById("vid").src='http://toplofty-rat-9906.dataplicity.io/?action=stream';
  document.getElementById("tools").disabled=false;
  document.getElementById("control").src='https://toplofty-rat-9906.dataplicity.io/control.htm';
    }
    if(resp == "error"){
    var ntt=document.getElementById("notifications").innerHTML;
    document.getElementById("notifications").innerHTML ="<li>"+"Time out"+"</li>"+ntt;
    mUp();
    }
    }
  };
  xhttp.open("get", "/camera_loading", true);
  xhttp.send();
  }
else{
  obj.style.backgroundColor="white";
  obj.style.borderColor = "black";
  document.getElementById("switch-point").style.backgroundColor="black";
  document.getElementById("switch-point").style.marginLeft="8%";
  document.getElementById("status").innerHTML="Off";
  document.getElementById("camoff").style.display="block";
  document.getElementById("loading").style.display="none";
  document.getElementById("vid").style.display="none";
  document.getElementById("vid").src='';
  document.getElementById("control").src='';
  document.getElementById("tools").disabled = true;
  var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    var nt=document.getElementById("notifications").innerHTML;
    document.getElementById("notifications").innerHTML ="<li>"+ this.responseText + "</li>"+nt;
    }
  };
  xhttp.open("GET", "/change_camera", true);
  xhttp.send();
 }
}

var disp="false"
function tool(){
if(disp=='true'){
document.getElementById("control").style.display='none';
disp='false'
}
else{
document.getElementById("control").style.display='block';
disp='true'
}
}

document.getElementById('current-link').innerHTML="Live Monitoring";
document.getElementById("tools").style.display='block';



