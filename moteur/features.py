import os



from playsound import playsound

import pywhatkit as kit

import webbrowser


from moteur.commend import speak
from moteur.database import*
from moteur.configeration import VOICE_ASSISTANT_NAME
from moteur.helper import extract_vedio_name

 # playinag ziko start sound function
def playSound():
    audio_dir ="site/assest/audio/zass start.mp3"
    playsound(audio_dir)





def openCommend(text):
    # Supprimez le nom de l'assistant vocal du texte
    text = text.replace(VOICE_ASSISTANT_NAME,"")
    # Supprimer le mot « open » du texte
    text = text.replace("open","")
    # Convertit le texte en minuscules
    text=text.lower()
    
    apk_name = text.strip()
    

    if apk_name != "":
        # Check if 'apk_name' exists in the 'sys_command' table
        try:
            curs.execute(
                'SELECT PATH FROM system_commend WHERE NAME IN (?)', (apk_name,))
            results = curs.fetchall()

            if len(results) != 0:
                speak("Opening "+text)
                os.startfile(results[0][0])
                print(1)

        # If 'apk_name' is not found in 'sys_command', check 'web_command' table
            elif len(results) == 0: 
                curs.execute(
                    'SELECT URL FROM web_commend WHERE NAME IN (?)', (apk_name,))
                results = curs.fetchall()
                
                if len(results) != 0:
                    speak("Opening " +text)
                    webbrowser.open(results[0][0])
                    print(2)


                else:
                     # If 'apk_name' is not found in both tables, try opening it directly
                    speak("Opening " +text)
                    try:
                        os.system('start ' +text)
                        print(3)

                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")









def playYoutube(text):
    # Extract the video name from the text command
   video_name= extract_vedio_name(text)

   speak("playing" +video_name +"in youtube")

    # Play the video on YouTube
   kit.playonyt(video_name)





