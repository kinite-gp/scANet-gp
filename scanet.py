from app import check,banner,tinput
from os import system

check.dependency()
banner.banner()
banner.menu()
menuVar = tinput.tinput('Home','Choose number')

if menuVar == '1':
    pass
elif menuVar == '2':
    pass
elif menuVar == '3':
    pass
elif menuVar == '4':
    pass
elif menuVar == '5':
    pass
elif menuVar == '0':
    system('cls')
    banner.banner()
    banner.menu_setting()
    menuVar = tinput.tinput('Home\\Setting', 'Choose number')
    if menuVar == '1':
        pass
    elif menuVar == '2':
        pass
    