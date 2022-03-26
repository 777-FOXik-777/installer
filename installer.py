import os, time, webbrowser

os.system('pip install colorama')
os.system('clear')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)

os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка утилит...")
res()
os.system('git clone https://github.com/th3unkn0n/osi.ig')
os.chdir('osi.ig')
os.system('python3 -m pip install -r requirements.txt')
os.system('git clone https://github.com/777-FOXik-777/installer')


os.system('clear')
print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка питон'v2'...")
res()
os.system('pkg install python2')
os.system('clear')


print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка забав...")
res()
os.system('pkg install cmatrix')

os.system('pkg install sl')
os.system('pkg install tty-clock')

os.system('pkg install libcaca -y')


os.system('clear')
print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка приветствия...")
res()
os.system('pkg install toilet')

os.system('rm ~/.bashrc')
os.system('echo "clear" >> ~/.bashrc')
os.system('echo "toilet -f mono9 -F metal hello" >> ~/.bashrc')
os.system('echo "echo [telegram @sypexhack желает вам хорошего дня]" >> ~/.bashrc')
os.system('echo "echo изменить приветствие можно в installer пункт [5]" >> ~/.bashrc')


os.system('clear')
print(Fore.GREEN+'[Запуск installer]')
res()
time.sleep(3)
os.system('python3 tool.py')
