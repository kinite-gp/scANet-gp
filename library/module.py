from datetime import datetime
import json
from playsound import playsound

def tinput(location='',qestion=''):
	print()
	inp = input(f'scANet|GP ~ {location} ╼\n{qestion}')
	print()
	return inp

def get_date_json():
    file = open('library\\setup.json','r')
    date = file.read()
    dict = json.loads(date)
    return dict

dict = get_date_json()
autsave = dict['autosave']
locsave = dict['locsave'] 
var = dict['sounds']

def autosave(target,text):
    if autsave != 'no' or autsave != 'No' or autsave != 'NO': 
        file = open(f'logs\\autosave\\{target}','a')
        file.write(f'{text}\n')
        file.close()
    else:
        pass

def writeout(target,text):
    if locsave != 'no' or locsave != 'No' or locsave != 'NO': 
        file = open(locsave+target,'a')
        file.write(f'{text}\n')
        file.close()
    else:
        pass

def log(log):
    var = datetime.now()
    timedate = var.strftime("%Y/%m/%d %H:%M:%S")
    logs = timedate +' >> '+log
    file = open('logs\\logs.txt','a')
    file.write(f'{logs}\n')
    file.close()
    
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