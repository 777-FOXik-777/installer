import os, time

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)

#колорам

os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка colorama...")
res()
time.sleep(1.5)
os.system('pip install colorama')

#питон

os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python2...")
res()
time.sleep(1.5)
os.system('pkg install python2')
os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python3...")
res()
time.sleep(1.5)
os.system('pkg install python3')

#запуск

os.system('clear')
os.system('python3 tool.py')
