from ast import Pass
from library import setup

dict = setup.get_date_json()
autsave = dict['autosave']
locsave = dict['locsave'] 

def autosave(target,text):
    if autsave != 'no' or autsave != 'No' or autsave != 'NO': 
        file = open(f'logs\\autosave\\{target}','a')
        file.write(f'{text}\n')
        file.close()
    else:
        Pass

def writeout(text):
    if locsave != 'no' or locsave != 'No' or locsave != 'NO': 
        file = open(locsave,'a')
        file.write(f'{text}\n')
        file.close()
    else:
        pass
