from colorama import Fore

def tinput(location='',qestion=''):
	inp = input('''
┌─( '''+Fore.CYAN+'''scANet|GP'''+Fore.RESET+''' ╼ ㉿ '''+Fore.RED+f'''{location} '''+Fore.RESET+''')
|  '''+Fore.GREEN+f'''{qestion}'''+Fore.RESET+'''
└──╼>> ''')
	return inp
