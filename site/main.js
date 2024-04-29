$(document).ready(function () {
    $('.startext').textillate({
      loop:true,
      sync:true,
      
      in:{
        effect:'bounceIn',
      },
      
      out:{
        effect:'bounceOut',
      }


    });

// ziko message Animation
    $('.zikoMsg').textillate({
      loop:true,
      sync:true,
      
      in:{
        effect:'fadeInUp',
        sync:true,
      },
      
      out:{
        effect:'fadeOutUp',
        sync:true,
      }


    });
   
  // siri cnfegation
  
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style:"ios9",
    amplitude:1,
    speed:0.30,
    autostart:true,
  });
 
// microphne  run clik 
    $('#MicButton').click( function (){
    $("#Oval").attr("hidden",true);
    $("#SiriWave").attr("hidden",false);
    eel.allCommends()()


  });

// microphne run shorts 
function keyshort(ke) {
  if (ke.ctrlKey && ke.key === 'Z') {     
      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.allCommends()();
  }
}

// Attach the keyup event listener to the document
document.addEventListener('keyup', keyshort);

// to play assisatnt 
function PlayAssistant(message) {

  if (message != "") {

      $("#Oval").attr("hidden", true);
      $("#SiriWave").attr("hidden", false);
      eel.allCommends(message);
      $("#chatbox").val("")
      $("#MicButton").attr('hidden', false);
      $("#sendButton").attr('hidden', true);

  }

}


 // toogle fucntion to hide and display mic and send button 
 function ShowHideButton(message) {
  if (message.length == 0) {
      $("#MicButton").attr('hidden', false);
      $("#sendButton").attr('hidden', true);
  }
  else {
      $("#MicButton").attr('hidden', true);
      $("#sendButton").attr('hidden', false);
  }
}

 // key up event handler on text box
 $("#chatbox").keyup(function () {

  let message = $("#chatbox").val();
  ShowHideButton(message)

});

// send button event handler
$("#sendButton").click(function () {

  let message = $("#chatbox").val()
  PlayAssistant(message)

});

// enter press event handler on chat box
$("#chatbox").keypress(function (e) {
  key = e.which;
  if (key == 13) {
      let message = $("#chatbox").val()
      PlayAssistant(message)
  }
});


});