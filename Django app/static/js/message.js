function iniDoc() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {}
  xhttp.open("GET", "/messagefunc", true);
  xhttp.send();
}
iniDoc();

function loadDoc() {
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {

var txt=this.responseText;
if(txt.length>=10){
    var newtxt=txt.split('~');
    var i;
    for(i=0;i < (newtxt.length -1);i++){
    var newvar = newtxt[i].split('/');
    var tabledata=document.getElementById("table").innerHTML;
    document.getElementById("table").innerHTML ="<tr>"+"<td class='time' style='background-color:rgb(151, 180, 118)'>"+newvar[0]+"</td>"+"<td class='message' style='background-color:rgb(151, 180, 118)'>"+newvar[1]+"</td>"+"</tr>"+tabledata;
    }
    }

    }
  };
  xhttp.open("GET", "/newmessages", true);
  xhttp.send();
}
window.setInterval(loadDoc, 1000);
document.getElementById('current-link').innerHTML='Messages';