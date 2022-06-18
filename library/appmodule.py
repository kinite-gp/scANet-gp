from library import module
import pyperclip
from os import system


def about():
    banner()
    print("""
           Thank you for using this tool.

              While reading this text,
   my github link has been copied in your system and
    you  can  use  it  and  give  us  encouragement.

         We are happy for you to submit your
          opinion with a star or a message

                     kinite-gp


                   press a key...
    """)  
    pyperclip.copy('https://github.com/kinite-gp')
    module.tinput('Home\\About','')

dict = module.get_date_json()
var = dict['appmode']

def banner():
    if var == 'app':
        system('cls')
    elif var == 'cli':
        pass
    module.welcome()
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
        """)

def menu():
    banner()
    print(
        """
1 ---------- Whois. ---------- get whois
2 ------- PortScanner. ------- scan port site
3 ----------- Help ----------- sea help
4 ---------- About! ---------- sea GitHub
5 --------- Setting! --------- sea settings / get log

Q ----------- Quit ----------- exit
        """)

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
        """)


def help():
    banner()
    print("""
Start scANet 
Get 'domin' & Starting scan
-----------------------------------
-----------------------------------
Help
Get help & Sea this page
-----------------------------------
-----------------------------------
About
Sea the GitHub link
-----------------------------------
-----------------------------------
Setting
Sea Setup & All logs
-----------------------------------


-----------------------------------
file log      > logs\\log.txt
Auto save     > logs\\autosave\\
Settings file > library\\setup.json
-----------------------------------
    """)
    module.tinput('Home\\Help','')
