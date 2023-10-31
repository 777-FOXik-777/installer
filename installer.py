import os, time

os.system('clear')
os.system('pip install colorama')
os.system('clear')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)

#обновление

os.system('rm -fr /data/data/com.termux/files/home/update.py')
  
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
os.system('xdg-open https://t.me/SYPEXHACK')
os.system('python3 tool.py')
