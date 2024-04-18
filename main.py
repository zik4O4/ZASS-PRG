import os

import eel

from moteur.features import *
from moteur.commend import *

def startVA():
    eel.init("SiteTest")



    os.system(' start msedge.exe --app="http://localhost:8000/index.html"')

    playSound()
    eel.start('index.html', mode=None, host='localhost', block=True)

startVA()

  