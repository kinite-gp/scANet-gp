from ast import Pass
from library import check,banner,tinput,sound,about,help,startscan

check.dependency()

while True:
    banner.menu()
    menuVar = tinput.tinput('Home','Choose> ')

    if menuVar == '1':
        startscan.scanrun()
    elif menuVar == '2':
        help.help()
    elif menuVar == '3':
        about.about()
    elif menuVar == '4':
        banner.setting()
        menuVar2 = tinput.tinput('Setting','Choose> ')
        if menuVar2 == '1':
            pass
        elif menuVar2 == "b" or menuVar2 == "B":
            pass
        elif menuVar == 'Q' or menuVar == 'q':
            sound.exit()
            exit()

    elif menuVar == 'Q' or menuVar == 'q':
        sound.exit()
        exit()

    