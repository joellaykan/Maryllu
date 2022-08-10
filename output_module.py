from speak_module  import speak
from database import speak_is_on
from system.screen_text import *

def output(o):

    #command line output
    cprint('(^-^)-> ' + o,choice(color))

    if speak_is_on():
        speak(o)

    print()
