document.getElementById('current-link').innerHTML='Serial Sender';

function send_cmd(){
        var cmd=document.getElementById('cmd_input').value;
        cmd=cmd.toUpperCase();
        document.getElementById('cmd-list').innerHTML += "<li>" + "> " + cmd +"</li>";
        document.getElementById('cmd_input').value='';
        if(document.getElementById('autoscroll').checked==true){
        document.getElementById('cmd-box').scrollTop=5000;
        }
        if(cmd.length>=1){
        cmd=cmd.replace(/\?/g,"%3f");
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        var resp = this.responseText;
        document.getElementById('cmd-list').innerHTML += "<li>"+ resp +"</li>";
        if(document.getElementById('autoscroll').checked==true){
        document.getElementById('cmd-box').scrollTop=5000;
        }

        }
        }
    };
  xhttp.open("GET", "/cmd_message/"+cmd, true);
  xhttp.send();

        }
        function clear_op(){
        document.getElementById('cmd-list').innerHTML='';
        }

        function scrollfunc(){
            document.getElementById('cmd-box').scrollTop=5000;
            }