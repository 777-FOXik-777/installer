import os, time

os.system('clear')
os.system('pip install colorama')
os.system('clear')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)


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

#забавы

os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка cmatrix...")
res()
time.sleep(1.5)
os.system('pkg install cmatrix')
os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка sl...")
res()
time.sleep(1.5)
os.system('pkg install sl')
os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка tty-clock...")
res()
time.sleep(1.5)
os.system('pkg install tty-clock')
os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка libcaca...")
res()
time.sleep(1.5)
os.system('pkg install libcaca -y')


os.system('clear')
print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка toilet...")
res()
time.sleep(1.5)
os.system('pkg install toilet -y')

#запуск

os.system('clear')
os.system('python3 start.py')
