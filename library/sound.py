from playsound import playsound
from library import setup

dict = setup.get_date_json()
var = dict['sounds']

def error():
    if var == 'on':
        playsound('library\\sounds\\error.wav')
    elif var == 'off':
        pass
def disconnect():
    if var == 'on':
        playsound('library\\sounds\\disconnect.wav')
    elif var == 'off':
        pass
def finish():
    if var == 'on':
        playsound('library\\sounds\\finish.wav')
    elif var == 'off':
        pass

def start():
    if var == 'on':
        playsound('library\\sounds\\start.wav')
    elif var == 'off':
        pass
def welcome():
    if var == 'on':
        playsound('library\\sounds\\welcome.wav')
    elif var == 'off':
        pass
def exit():
    if var == 'on':
        playsound('library\\sounds\\exit.wav')
    elif var == 'off':
        pass
def recycle():
    if var == 'on':
        playsound('library\\sounds\\recycle.wav')
    elif var == 'off':
        pass