import pyttsx3

import speech_recognition as sr

import eel

import time



def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # changer le voix Masculin[0]//fiminin[1]
    engine.setProperty('voice', voices[0].id)

    # la vietess de voix
    engine.setProperty('rate',174)
    engine.say(text)
    eel.DisplayMessage("ZASS "+text)
    engine.runAndWait()




@eel.expose
def takeCommend():
   
    # Create a recognizer object
   reco = sr.Recognizer()

    # Use the default microphone as the audio source
   with sr.Microphone() as source:
        print("Listening...")

     #    afficher le text dans siri wave
        eel.DisplayMessage("Listening...")

        reco.pause_threshold = 1

        # Adjust for ambient noise before recording
        reco.adjust_for_ambient_noise(source)

         # Record audio from the microphone
        audio = reco.listen(source, 10,6)
        
   try:
        print("Recognition processing...")

     #    afficher le text dans siri wave
        eel.DisplayMessage("Recognition processing...")

        # Recognize speech using Google Speech Recognition
        text = reco.recognize_google(audio ,language="en")
         
        print(f"You said: {text}")
        
     #    afficher le text dans siri wave
        eel.DisplayMessage(text)
        time.sleep(2)
     # return to reception 
        eel.reception_back()


   except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        eel.DisplayMessage("Sorry, I couldn't understand what you said.")
        eel.reception_back()

   except sr.RequestError as e:
        print(f"Error fetching results from Google Speech Recognition service: {e}")
        eel.reception_back()

        
   return text



@eel.expose
def allCommends():
     try:
          text=takeCommend()
          print(text)

          if "open" in text:
               from moteur.features import openCommend
               openCommend(text)
          elif "on youtube" in text:
               from moteur.features import playYoutube
               playYoutube(text)
          elif "send message" in text or "phone call" in text or "video call" in text:
            from moteur.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(text)
            if(contact_no != 0):

                if "send message" in text:
                    flag = 'message'
                    speak("what message to send")
                    text=takeCommend()
                    
                elif "phone call" in text:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, text, flag, name)
          else:
               print("not run in allcommend ")     
     except :
      print("errur in allcommend ")



