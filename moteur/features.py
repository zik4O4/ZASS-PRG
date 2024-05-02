import os
from pipes import quote
import struct
import subprocess
import time



from playsound import playsound

import pyaudio
import pyautogui
import pywhatkit as kit

import webbrowser


from moteur.commend import speak
from moteur.database import*
from moteur.configeration import VOICE_ASSISTANT_NAME
from moteur.helper import extract_vedio_name, remove_words

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

def word_detection():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=porcupine.create(keywords=["alexa","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("Z")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# Whatsapp Message Sending

# findContact
def findContact(query):
    
    
    words_to_remove = [VOICE_ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        curs.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = curs.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        # if not mobile_number_str.startswith('+212'):
        #     mobile_number_str = '+212' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
    
# Whatsapp Function
def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        zass_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        zass_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        zass_message = "staring video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(zass_message)


