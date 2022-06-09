from os import system
from time import sleep
from subprocess import Popen
from tabulate import tabulate

def banner():
    system("cls")
    print("")
    Popen('neofetch')
    sleep(2)

def menu():
    table = [
        ["1","Fast Scan"],
        ["2","Full Scan"],
        ["3","Choose Scan"],
        ["4","About"],
        ["5","Help"],
        ["0","Setting"],
        ["",""],
        ["Q","Exit"]
    ]
    menu = tabulate(table,headers=["---","--------------------------"])
    print(menu)

def menu_setting():
    table = [
        ["1","Open Settings"],
        ["2","Sea logs"],
    ]
    menu = tabulate(table,headers=["---","--------------------------"])
    print(menu)
