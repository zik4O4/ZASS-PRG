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







});