import os
import struct
import time

from playsound import playsound

import pywhatkit as kit

import webbrowser

import pvporcupine

import pyaudio

from engine.commend import speak
from engine.database import*
from engine.configeration import VOICE_ASSISTANT_NAME
from engine.helper import extract_vedio_name

 # playinag ziko start sound function
def playZikoSound():
    audio_dir ="SiteTest/assest/audio/ziko start.mp3"
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
        porcupine=pvporcupine.create(keywords=["alexa","alexa"]) 
        paud=pyaudio.PyAudio()
        
        # Open an audio stream for recording
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
                autogui.press("z")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()


