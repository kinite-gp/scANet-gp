def dependency():
    try:
        from datetime import datetime
        import json
        from playsound import playsound
    except ImportError:
        exit('please install library "pip install requirments.txt"')
dependency()
from library import module,appmodule,startscan

while True:
    appmodule.menu()
    menuVar = module.tinput('Home','Choose> ')

    if menuVar == '1':
        startscan.whoisrun()
    elif menuVar == '2':
        pass # port scanner
    elif menuVar == '3':
        appmodule.help()
    elif menuVar == '4':
        appmodule.about()
    elif menuVar == '5':
        appmodule.setting()
        menuVar2 = module.tinput('Setting','Choose> ')
        if menuVar2 == '1':
            appmodule.banner()
            loging = open('logs\\logs.txt','r')
            print(loging)
            module.tinput()
        elif menuVar2 == "b" or menuVar2 == "B":
            pass
        elif menuVar == 'Q' or menuVar == 'q':
            module.exit()
            exit()

    elif menuVar == 'Q' or menuVar == 'q':
        module.exit()
        exit()

    