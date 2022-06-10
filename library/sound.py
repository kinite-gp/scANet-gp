from playsound import playsound
from library import setup

dict = setup.get_date_json()
var = dict['sounds']

def error():
    if var == 'on':
        playsound('library\\sounds\\error.wav')
    else:
        pass
def disconnect():
    if var == 'on':
        playsound('library\\sounds\\disconnect.wav')
    else:
        pass
def finish():
    if var == 'on':
        playsound('library\\sounds\\finish.wav')
    else:
        pass
def start():
    if var == 'on':
        playsound('library\\sounds\\start.wav')
    else:
        pass
def welcome():
    if var == 'on':
        playsound('library\\sounds\\welcome.wav')
    else:
        pass
def exit():
    if var == 'on':
        playsound('library\\sounds\\exit.wav')
    else:
        pass
def recycle():
    if var == 'on':
        playsound('library\\sounds\\recycle.wav')
    else:
        pass