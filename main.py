import os

import eel

from engine.features import *
from engine.commend import *

def startVA():
    eel.init("SiteTest")



    os.system(' start msedge.exe --app="http://localhost:8000/index.html"')

    playZikoSound()
    eel.start('index.html', mode=None, host='localhost', block=True)

startVA()

  