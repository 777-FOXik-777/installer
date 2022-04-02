import os, time, webbrowser

from colorama import Fore, Style, Back

print ('\n')
def res():
    print(Style.RESET_ALL)

os.system('clear')
print('Добро пожаловать в..')
time.sleep(3)

while True:
    os.system('clear')
    print(Back.RED)
    print(Fore.BLACK+'АДСКИЙ TERMUX')
    res()
    print(Fore.YELLOW+'[1] сыграть')
    print(Fore.YELLOW+'[0] выйти')
    res()
    tsu = input('выберете пункт>>> ')
    if tsu == '1':
        os.system

    if tsu == '0':
        os.system('python3 tool.py')
    else:
        os.system('clear')
