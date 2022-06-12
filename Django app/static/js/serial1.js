var input = document.getElementById("cmd_input");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
   event.preventDefault();
   document.getElementById("send-button").click();
  }
});
