import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

def res():
    print(Style.RESET_ALL)

def baner():
    os.system('clear')
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
    print(Style.BRIGHT, Fore.CYAN+"[+Fore.YELLOW+Github.com/777-FOXik-777/installer+Fore.YELLOW+]        ["+Fore.YELLOW+"Настройки"+Fore.CYAN+"]")
    res()
    print(Fore.GREEN+"    [1] Запускать Installer вместе с Termux")
    print(Fore.GREEN+"    [2] Обновить/Переустановить Installer")
    print(Fore.GREEN+"    [3] Установить последнюю версию Termux")
    print(Fore.GREEN+"    [4] Переместить скачаные директории в /files/home/")
    print(Fore.GREEN+"    [5] Добавить утилиту в Installer")
    print(Fore.GREEN+"    [6] Удалить скачаные директории")
    print(Fore.CYAN+"")
    print(Fore.YELLOW+"    [h] Сообщить об ошибке")
    print(Fore.YELLOW+"    [e] Назад")
    res()
    inp = input('  Выбери пункт>>> ')
    os.system('clear')


    
    if inp == '1':
        os.system('clear')
        baner()
        print (Fore.CYAN+'\n Запускать Installer вместе с Termux?')
        res()
        print(Fore.YELLOW+'    [1]'+Fore.YELLOW+' Включить')
        print(Fore.YELLOW+'    [2]'+Fore.YELLOW+' Выключить')
        res()
        print(Fore.YELLOW+'    [e] выход')
        res()
        tru_101 = input('  Выбери пункт>>> ')

        if tru_101 == '1':
            os.system('echo "cd && cd installer && python tool.py" >> ~/.bashrc')
            os.system('clear')
            baner()
            res()
            print(Fore.GREEN+"\n  Включено!")
            res()
            tsu_103 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        if tru_101 == '2':
            os.system('rm ~/.bashrc')
            os.system('clear')
            baner()
            res()
            print(Fore.YELLOW+"\n  Выключено!")
            res()
            tsu_103 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        else:
            os.system('clear')


    
    if inp == '2':
        os.system('clear')
        baner()
        print(Fore.CYAN+'\n Вы хотите Обновить/Переустановить Installer?')
        print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Все файлы в директории Installer удалятся!')
        res()
        tru_201 = input('  Продолжить? [y/n] >>> ')
        if tru_201 == 'y':
            os.system('mv update.py /data/data/com.termux/files/home/')
            os.system('rm ~/.bashrc')
            os.system('echo "cd && python update.py" >> ~/.bashrc')
            while True:
                os.system('clear')
                print(Fore.YELLOW+'\n Перезапустите Termux или создайте новый сезон!')
                tru_202 = input('')
        else:
            os.system('clear')


    
    if inp == '3':
        os.system('xdg-open https://t.me/SYPEXHACK_fail/51')
        os.system('clear')


    
    if inp == '4':
        os.system('clear')
        baner()
        print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Переместить скачаные директории в /files/home ?')
        res()
        tru_401 = input('  Выбери пункт [y/n] >>> ')
        if tru_401 == 'y':
            os.system('mv PyPhisher /data/data/com.termux/files/home/')
            os.system('mv zphisher /data/data/com.termux/files/home/')
            os.system('mv maskphish /data/data/com.termux/files/home/')
            os.system('mv seeker /data/data/com.termux/files/home/')
            os.system('mv CamPhish /data/data/com.termux/files/home/')
            os.system('mv TigerVirus /data/data/com.termux/files/home/')
            os.system('mv CamHacker /data/data/com.termux/files/home/')
            os.system('mv VidPhisher /data/data/com.termux/files/home/')
            os.system('clear')
            baner()
            res()
            print(Fore.GREEN+"\n Все директории УСПЕШНО перенесены в папку /files/home/")
            res()
            tsu_402 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')

        else:
            os.system('clear')


    
    if inp == '5':
        os.system('xdg-open https://forms.gle/vMHny8Yp24HQZqLV9')
        os.system('clear')


    
    
    if inp == '6':
            baner()
            print (Fore.CYAN+'\n Где именно удалить директории?')
            res()
            print(Fore.YELLOW+'    [1]'+Fore.YELLOW+' В папке /files/home/')
            print(Fore.YELLOW+'    [2]'+Fore.YELLOW+' В директории installer')
            print(Fore.YELLOW+'    [3]'+Fore.YELLOW+' Везде')
            print(Fore.YELLOW+'')
            print('    [e] выход')
            res()
            tru_602 = input('  Выбери пункт>>> ')
    
            if tru_602 == '1':
                os.system('clear')
                baner()
                print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Вы уверены что хотите удалить директории в папке /files/home/?')
                res()
                tru_603 = input('  Продолжить [y/n] >>> ')
                if tru_603 == 'y':
                    os.system('clear')
                    os.system('rm -fr /data/data/com.termux/files/home/PyPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/maskphish')
                    os.system('rm -fr /data/data/com.termux/files/home/seeker')
                    os.system('rm -fr /data/data/com.termux/files/home/CamPhish')
                    os.system('rm -fr /data/data/com.termux/files/home/zphisher')
                    os.system('rm -fr /data/data/com.termux/files/home/TigerVirus')
                    os.system('rm -fr /data/data/com.termux/files/home/CamHacker')
                    os.system('rm -fr /data/data/com.termux/files/home/VidPhisher')
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+"\n Все директории в папке /files/home/ УСПЕШНО удалены!")
                    res()
                    tsu_603 = input(' [Нажмите enter чтобы выйти]')
                    os.system('clear')

                else:
                    os.system('clear')
        
            if tru_602 == '2':
                os.system('clear')
                baner()
                print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Вы уверены что хотите удалить директории в директории installer?')
                res()
                tru_603 = input('  Продолжить [y/n] >>> ')
                if tru_603 == 'y':
                    os.system('rm -fr /data/data/com.termux/files/home/installer/PyPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/maskphish')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/seeker')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/CamPhish')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/zphisher')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/TigerVirus')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/CamHacker')
                    os.system('rm -fr /data/data/com.termux/files/home/installer/VidPhisher')
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+"\n Все директории в директории installer УСПЕШНО удалены!")
                    res()
                    tsu_503 = input(' [Нажмите enter чтобы выйти]')
                    os.system('clear')

                else:
                    os.system('clear')

    
            if tru_602 == '3':
                os.system('clear')
                baner()
                print(Fore.WHITE+'\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] Вы уверены что хотите удалить все директории?')
                res()
                tru_603 = input('  Продолжить [y/n] >>> ')
                if tru_603 == 'y':
                    os.system('rm -fr /data/data/com.termux/files/home/PyPhisher && rm -fr /data/data/com.termux/files/home/installer/PyPhisher')
                    os.system('rm -fr /data/data/com.termux/files/home/zphisher && rm -fr /data/data/com.termux/files/home/installer/zphisher')
                    os.system('rm -fr /data/data/com.termux/files/home/maskphish && rm -fr /data/data/com.termux/files/home/installer/maskphish')
                    os.system('rm -fr /data/data/com.termux/files/home/seeker && rm -fr /data/data/com.termux/files/home/installer/seeker')
                    os.system('rm -fr /data/data/com.termux/files/home/CamPhish && rm -fr /data/data/com.termux/files/home/installer/CamPhish')
                    os.system('rm -fr /data/data/com.termux/files/home/TigerVirus && rm -fr /data/data/com.termux/files/home/installer/TigerVirus')
                    os.system('rm -fr /data/data/com.termux/files/home/CamHacker && rm -fr /data/data/com.termux/files/home/installer/CamHacker')
                    os.system('rm -fr /data/data/com.termux/files/home/VidPhisher && rm -fr /data/data/com.termux/files/home/installer/VidPhisher')
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+"\n Все директории УСПЕШНО удалены!")
                    res()
                    tsu_503 = input(' [Нажмите enter чтобы выйти]')
                    os.system('clear')

                else:
                    os.system('clear')

            else:
                os.system('clear')


    
    if inp == 'h':
        os.system('xdg-open https://t.me/SYPEXHACK_help_bot')
        os.system('clear')

    
    
    if inp == 'e':
        res()
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('clear')
        break
