import os, time

#colorama

os.system('clear')
os.system('cd && cd installer')

print ('[~] Установка colorama... \n')
time.sleep(1.5)
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

#доступ к файлам

os.system('clear')
print (Fore.YELLOW+"["+Fore.CYAN+"!"+Fore.YELLOW+"] Разрешите доступ к файлам")
res()
time.sleep(1.5)
os.system('termux-setup-storage')
tsu = input('\n[Нажмите enter чтобы продолжить]')
os.system('clear')
            
#запуск

os.system('clear')
os.system('xdg-open https://t.me/+p9CBKAxQUQZmMjli')
os.system('python3 tool.py')
