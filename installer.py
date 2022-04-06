import os, time

os.system('clear')
os.system('pip install colorama')
os.system('clear')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)

os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка питон'v2'...")
res()
time.sleep(1.5)
os.system('pkg install python2')
os.system('pkg install python3')
os.system('clear')


print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка забав...")
res()
time.sleep(1.5)
os.system('pkg install cmatrix')
os.system('pkg install sl')
os.system('pkg install tty-clock')
os.system('pkg install libcaca -y')

os.system('clear')
print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка приветствия...")
res()
time.sleep(1.5)
os.system('pkg install toilet')


os.system('clear')
print(Fore.GREEN+'[Запуск installer]')
res()
time.sleep(3)
os.system('python3 tool.py')
