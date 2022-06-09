from subprocess import getoutput
from os import system


def dependency():


    result = getoutput("neofetch")
    if "not found" in result:
        input('Connect To Internet >> Press Enter')
        system('pip install neofetch-win')
        exit()

    try:
        from colorama import Fore,Style

    except ImportError:
        input('Connect To Internet >> Press Enter')
        system('python3 -m pip install -r requirments.txt')
        exit()

    