from os import system
from library import sound,setup

dict = setup.get_date_json()
var = dict['appmode']

def banner():
    if var == 'app':
        system('cls')
    elif var == 'cli':
        pass
    sound.welcome()
    print(
        """
                       d8888888b    888        888    
                      d888888888b   888        888    
                     d88P88888888b  888        888    
.d8888b  .d8888b    d88P 888888Y88b 888 .d88b. 888888 
88K     d88P"      d88P  888888 Y88b888d8P  Y8b888    
"Y8888b.888       d88P   888888  Y8888888888888888    
     X88Y88b.    d8888888888888   Y8888Y8b.    Y88b.  
 88888P' "Y8888Pd88P     888888    Y888 "Y8888  "Y888 
        """
    )

def menu():
    banner()
    print(
        """
1 ------- Start scANet ------- run scripts
2 ----------- Help ----------- sea help
3 ---------- About! ---------- sea GitHub
4 --------- Setting! --------- sea settings / get log

Q ----------- Quit ----------- exit
        """
    )

def setting():
    banner()
    print(
    f"""
* ---------- Sounds ---------- {dict['sounds']}
* ----------- mood ----------- {dict['appmode']}
* --------- AutoSave --------- {dict['autosave']}
* -------- ExportSave -------- {dict['locsave']}
    
1 ----------- logs ----------- print logs

B ----------- Back ----------- go back
Q ----------- Quit ----------- exit
        """
    )
