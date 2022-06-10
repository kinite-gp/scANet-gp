from library import check,banner,tinput,sound,about,help
from os import system

check.dependency()

while True:
    banner.banner()
    banner.menu()
    menuVar = tinput.tinput('Home','Choose> ')

    if menuVar == '1':
        pass
    elif menuVar == '2':
        pass
    elif menuVar == '3':
        help.help()
    elif menuVar == '4':
        about.about()
    elif menuVar == 'Q' or menuVar == 'q':
        sound.exit()
        exit()

    