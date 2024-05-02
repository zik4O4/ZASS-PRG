$(document).ready(function () {
 
    // chnager the message of ZASS
     eel.expose(DisplayMessage)
     function DisplayMessage(message) {
 
         $(".zikoMsg li:first").text(message);
         $('.zikoMsg').textillate('start');
 
     }

     

     eel.expose(reception_back)
     function reception_back() {
 
        $("#Oval").attr("hidden",false);
        $("#SiriWave").attr("hidden",true);
     }





     eel.expose(senderText)
     function senderText(message) {
         var chatBox = document.getElementById("chat-canvas-body");
         if (message.trim() !== "") {
             chatBox.innerHTML += `<div class="row justify-content-end mb-4">
             <div class = "width-size">
             <div class="sender_message">${message}</div>
             </div>
         </div>`; 
     
             // Scroll to the bottom of the chat box
             chatBox.scrollTop = chatBox.scrollHeight;
         }
     }
 
     eel.expose(receiverText)
     function receiverText(message) {
 
         var chatBox = document.getElementById("chat-canvas-body");
         if (message.trim() !== "") {
             chatBox.innerHTML += `<div class="row justify-content-start mb-4">
             <div class = "width-size"  style="display: flex;"><i class="bi bi-robot" id="icon"></i>
             <div class="receiver_message">${message}</div>
             </div>
         </div>`; 
     
             // Scroll to the bottom of the chat box
             chatBox.scrollTop = chatBox.scrollHeight;
         }
         
     }
 



});