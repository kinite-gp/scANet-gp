from playsound import playsound
from library import setup

dict = setup.get_date_json()
var = dict['sounds']

def error():
    if var == 'yes':
        playsound('library\\sounds\\error.wav')
    elif var == 'off':
        pass
def disconnect():
    if var == 'yes':
        playsound('library\\sounds\\disconnect.wav')
    elif var == 'off':
        pass
def finish():
    if var == 'yes':
        playsound('library\\sounds\\finish.wav')
    elif var == 'off':
        pass

def start():
    if var == 'yes':
        playsound('library\\sounds\\start.wav')
    elif var == 'off':
        pass
def welcome():
    if var == 'yes':
        playsound('library\\sounds\\welcome.wav')
    elif var == 'off':
        pass
def exit():
    if var == 'yes':
        playsound('library\\sounds\\exit.wav')
    elif var == 'off':
        pass
def recycle():
    if var == 'yes':
        playsound('library\\sounds\\recycle.wav')
    elif var == 'off':
        pass