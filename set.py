import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

def res():
    print(Style.RESET_ALL)
    
while True:
    print(Fore.CYAN+'', Style.BRIGHT)
    print (" ___                 _             _   _               ")
    print ("|_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print (" | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print (" | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print ("\n")
    print ("[Telegram: @SYPEXHACK]                       [v2.7.1]")
    res()
    print (Fore.GREEN+"    [1] Ngrok      >>  Тунелирование")
    print (Fore.GREEN+"    [2] Localhost  >>  Тунелирование")
    print (Fore.GREEN+"    [3] PyPhiser   >>  Фишинг")
    print (Fore.GREEN+"    [4] Android    >>  Вирус ссылка")
    print (Fore.GREEN+"    [5] Maskphish  >>  Замаскировать ссылку")
    print (Fore.GREEN+"    [6] IP-Tracer  >>  Пробив по IP")
    print (Fore.GREEN+"    [7] Seeker     >>  Узнать местоположения")
    print (Fore.CYAN+"")
    print (Fore.YELLOW+'    [c] Официальный чат')
    print (Fore.YELLOW+'    [e] Выход')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '1':
