import os, time

from colorama import Fore, Style

os.system('cd /data/data/com.termux/files/home/installer/')
os.system('clear')

def res():
    print(Style.RESET_ALL)

def baner():
    print(Fore.CYAN+'', Style.BRIGHT)
    print('')
    print("  ___                 _             _   _               ")
    print(" |_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print("  | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print("  | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print(" |___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    res()
    
while True:
    baner()
    print(Style.BRIGHT, Fore.CYAN+"[Telegram: @SYPEXHACK]                         [v2.8.1]")
    res()
    print(Fore.GREEN+"    [1] Тест      >>  Тест")
    print(Fore.CYAN+"")
    print(Fore.YELLOW+"    [s] Настройки")
    print(Fore.YELLOW+"    [e] На главную")
    res()
    inp = input('  Выбери пункт>>> ')
    os.system('clear')

    

    if inp == 'a':
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('python tool.py')

    
    if inp == 's':
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('python set.py')

    

    if inp == 'e':
        os.system('clear')
        break
        os.system('python set.py')
