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





});