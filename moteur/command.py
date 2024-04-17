import pyttsx3 
def speak(text):
    engine = pyttsx3.init()
#getting details of current voice
    voices = engine.getProperty('voices') 
#changing index, changes voices.3 for male & 1 for female
    engine.setProperty('voice', voices[3].id) 
# setting up new voice rate
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()



speak("hello i'm Zass")
