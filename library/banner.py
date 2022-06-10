from os import system
from time import sleep
from subprocess import Popen
from tabulate import tabulate

def banner():
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
    print(
        """
        1 ------------------------ Start scANet
        2 ------------------------- Get proxys
        3 ---------------------------- Help
        4 --------------------------- About!

        Q ---------------------------- Quit
        """
    )

def setting():
    print(
        """
        1 --------------------------- Sounds
        2 --------------------------- Proxy!
        3 ---------------------------- mood
        4 ---------------------------- logs
        5 -------------------------- Auto save
        6 ------------------------- Export save

        B ---------------------------- Back
        Q ---------------------------- Quit
        """
    )
