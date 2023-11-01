import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

def res():
    print(Style.RESET_ALL)
    
while True:
    print('')
    print(Fore.CYAN+'', Style.BRIGHT)
    print(" ___                 _             _   _               ")
    print("|_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print(" | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print(" | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print("|___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print("\n")
    print("[Настройки]                                    [v2.7.1]")
    res()
    print(Fore.GREEN+"    [1] Запускать Installer вместе с Termux")
    print(Fore.GREEN+"    [2] Обновить/Проверить обновления Installer")
    print(Fore.GREEN+"    [3] Установить последнюю версию Termux")
    print(Fore.GREEN+"    [4] Копировать скачаные директории в /files/home/")
    print(Fore.CYAN+"")
    print(Fore.YELLOW+'    [e] Назад')
    res()
    inp = input('  Выбери пункт>>> ')
    os.system('clear')


    
    if inp == '1':
        os.system('clear')
        print (Fore.CYAN+'\n Запускать Installer вместе с Termux?')
        res()
        print(Fore.YELLOW+' [1]'+Fore.GREEN+' Включить')
        res()
        print(Fore.YELLOW+' [2]'+Fore.RED+' Выключить')
        print(Fore.YELLOW+'')
        print(' [e] выход')
        res()
        tru_101 = input(' Выбери пункт>>> ')

        if tru_101 == '1':
            os.system('clear')
            os.system('echo "cd && cd installer && python tool.py" >> ~/.bashrc')
            os.system('clear')
            print(Fore.GREEN+"\n  Включено!")
            res()
            tsu_103 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        if tru_101 == '2':
            os.system('clear')
            os.system('rm ~/.bashrc')
            os.system('clear')
            print(Fore.YELLOW+"\n  Выключено!")
            res()
            tsu_103 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        else:
            os.system('clear')


    
    if inp == '2':
        os.system('clear')
        print(Fore.CYAN+'\n Вы хотите обновить/проверить обновления Installer?')
        print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Все установлинные вами настройки сбросятся')
        res()
        tru_201 = input(' Начать [y/n] >>> ')
        if tru_201 == 'y':
            os.system('mv update.py /data/data/com.termux/files/home/')
            os.system('echo "cd && python update.py" >> ~/.bashrc')
            while True:
                os.system('clear')
                print(Fore.YELLOW+'\n Перезапустите Termux или создайте новый сезон!')
                tru_202 = input('')
        else:
            os.system('clear')


    
    if inp == '3':
        os.system('xdg-open https://t.me/SYPEXHACK_fail/51')


    
    if inp == 'e':
        res()
        os.system('clear')
        break
