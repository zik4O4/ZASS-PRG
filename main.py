import eel
import os
from moteur.features import *

eel.init("site")

os.system(' start msedge.exe --app="http://localhost:8000/index.html"')
playZASSsound()  
eel.start('index.html', mode=None, host='localhost', block=True)