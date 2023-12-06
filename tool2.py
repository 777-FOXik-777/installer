import os, time

from colorama import Fore, Style

os.system('cd /data/data/com.termux/files/home/installer/')
os.system('clear')

def pri():
    print(f'\33]0; Installer - Страница [2]\a',
                      end='', flush=True)


def res():
    print(Style.RESET_ALL)

def baner():
    os.system('clear')
    print(Fore.CYAN+'', Style.BRIGHT)
    print("  ___                 _             _   _               ")
    print(" |_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print("  | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print("  | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print(" |___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    res()
    
while True:
    os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
    
    filename = "holehe"
    if os.path.exists(filename):
      Holehe = ""+Fore.RED+"X"
    else:
      Holehe = ""+Fore.GREEN+"✓"
    
    os.chdir('/data/data/com.termux/files/home/Installer_Files')
    
    filename = "CamHacker"
    if os.path.exists(filename):
      CamHacker = ""+Fore.GREEN+"✓"
    else:
      CamHacker = ""+Fore.RED+"X"
    
    filename = "VidPhisher"
    if os.path.exists(filename):
      VidPhisher = ""+Fore.GREEN+"✓"
    else:
      VidPhisher = ""+Fore.RED+"X"
    
    filename = "Telephish"
    if os.path.exists(filename):
      Telephish = ""+Fore.GREEN+"✓"
    else:
      Telephish = ""+Fore.RED+"X"
    
    filename = "Dnnme2"
    if os.path.exists(filename):
      Dnnme2 = ""+Fore.GREEN+"✓"
    else:
      Dnnme2 = ""+Fore.RED+"X"
    
    filename = "Discord-Nitro-Generator-and-Checker"
    if os.path.exists(filename):
      Discord = ""+Fore.GREEN+"✓"
    else:
      Discord = ""+Fore.RED+"X"
    
    filename = "shorturl"
    if os.path.exists(filename):
      ShortUrl = ""+Fore.GREEN+"✓"
    else:
      ShortUrl = ""+Fore.RED+"X"

    filename = "PhoneInfoga"
    if os.path.exists(filename):
      PhoneInfoga = ""+Fore.GREEN+"✓"
    else:
      PhoneInfoga = ""+Fore.RED+"X"
    
    os.chdir('/data/data/com.termux/files/home/installer')
    pri()
    baner()
    print(Style.BRIGHT, Fore.CYAN+"[Telegram: @SYPEXHACK]                         ["+Fore.YELLOW+"2.10.1"+Fore.CYAN+"]")
    res()
    print(Fore.GREEN+"    [11] CamHacker  ("+CamHacker+""+Fore.GREEN+")  >>  Фото фишинг")
    print(Fore.GREEN+"    [12] VidPhisher ("+VidPhisher+""+Fore.GREEN+")  >>  Видео фишинг")
    print(Fore.GREEN+"    [13] Telephish  ("+Telephish+""+Fore.GREEN+")  >>  Фишинг в тг (1)")
    print(Fore.GREEN+"    [14] Dnnme2     ("+Dnnme2+""+Fore.GREEN+")  >>  Фишинг в тг (2)")
    print(Fore.GREEN+"    [15] Discord    ("+Discord+""+Fore.GREEN+")  >>  Генератор Nitro")
    print(Fore.GREEN+"    [16] ShortUrl   ("+ShortUrl+""+Fore.GREEN+")  >>  Сокращение ссылок")
    print(Fore.GREEN+"    [17] PhoneInfo  ("+PhoneInfoga+""+Fore.GREEN+")  >>  Инфо о номере")
    res()
    print(Style.BRIGHT,Fore.CYAN+"   [20] Страница (3)")
    res()
    print(Fore.YELLOW+"    [s] Настройки")
    print(Fore.YELLOW+"    [e] Назад")
    res()
    inp = input(' Выбери пункт>>> ')
    os.system('clear')
    


    if inp == '11':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
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
            res()
            tsu_102 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] CamHacker еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка CamHacker...")
            res()
            os.system('git clone https://github.com/KasRoudra/CamHacker')
            os.chdir('CamHacker')
            os.system('clear')
            os.system('bash ch.sh')
            res()
            tsu_102 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')



    if inp == '12':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
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
            res()
            tsu_202 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] VidPhisher еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка VidPhisher...")
            res()
            os.system('git clone https://github.com/KasRoudra/VidPhisher')
            os.chdir('VidPhisher')
            os.system('clear')
            os.system('bash vp.sh')
            res()
            tsu_202 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')



    if inp == '13':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
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
            os.system('python Instagram.py')
            os.system('clear')
            baner()
            os.system('python vk.py')
            os.system('clear')
            baner()
            os.system('python tiktok.py')
            os.system('rm -fr Instagram.py')
            os.system('rm -fr vk.py.py')
            os.system('rm -fr tiktok.py')
            os.system('clear')
            res()
            tsu_302 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Telephish еще НЕ установлен!")
            time.sleep(2)
            
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
            os.system('python Instagram.py')
            os.system('clear')
            baner()
            os.system('python vk.py')
            os.system('clear')
            baner()
            os.system('python tiktok.py')
            os.system('rm -fr Instagram.py')
            os.system('rm -fr vk.py.py')
            os.system('rm -fr tiktok.py')
            os.system('clear')
            res()
            tsu_302 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')



    if inp == '14':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "Dnnme2"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Dnnme2 уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('Dnnme2')
            os.system('clear')
            os.system('python build.py')
            os.system('clear')
            baner()
            os.system('python probiv.py')
            os.system('clear')
            baner()
            os.system('python nacr.py')
            os.system('clear')
            baner()
            os.system('python brawl.py')
            os.system('clear')
            baner()
            os.system('python znak.py')
            os.system('clear')
            baner()
            os.system('python btc.py')
            os.system('rm -fr nacr.py')
            os.system('rm -fr probiv.py')
            os.system('rm -fr brawl.py')
            os.system('rm -fr znak.py')
            os.system('rm -fr btc.py')
            os.system('clear')
            res()
            tsu_302 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Dnnme2 еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка pyTelegramBotAPI...")
            res()
            os.system('pip install pyTelegramBotAPI')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Dnnme2...")
            res()
            os.system('git clone https://github.com/lamer112311/Dnnme2')
          
            os.chdir('Dnnme2')
            os.system('clear')
            os.system('python build.py')
            os.system('clear')
            baner()
            os.system('python probiv.py')
            os.system('clear')
            baner()
            os.system('python nacr.py')
            os.system('clear')
            baner()
            os.system('python brawl.py')
            os.system('clear')
            baner()
            os.system('python znak.py')
            os.system('clear')
            baner()
            os.system('python btc.py')
            os.system('rm -fr nacr.py')
            os.system('rm -fr probiv.py')
            os.system('rm -fr brawl.py')
            os.system('rm -fr znak.py')
            os.system('rm -fr btc.py')
            os.system('clear')
            res()
            tsu_302 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')


  
    if inp == '15':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
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
            res()
            tsu_502 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Discord-Nitro-Generator еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests...")
            res()
            os.system('pip install requests')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка discord_webhook...")
            res()
            os.system('pip install discord_webhook')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка colored...")
            res()
            os.system('pip install colored')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка numpy...")
            res()
            os.system('pkg install python-numpy -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Discord-Nitro-Generator...")
            res()
            os.system('git clone https://github.com/logicguy1/Discord-Nitro-Generator-and-Checker.git')
            os.chdir('Discord-Nitro-Generator-and-Checker')
            os.system('clear')
            os.system('python3 main.py')
            res()
            tsu_502 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

    
    
    if inp == '16':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "shorturl"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] ShortUrl уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.system('ShortUrl')
            res()
            tsu_102 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] ShortUrl еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка ShortUrl...")
            res()
            os.system('git clone https://github.com/htr-tech/shorturl')
            os.chdir('shorturl')
            os.system('clear')
            os.system('bash setup.sh')
            os.system('ShortUrl')
            res()
            tsu_102 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')


    
    if inp == '17':
        os.chdir('/data/data/com.termux/files/home/Installer_Files')
        filename = "PhoneInfoga"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Phoneinfoga уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            os.chdir('PhoneInfoga')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"\n  [PhoneInfoga]")
            res()
            print(Fore.GREEN+'  Введите телефон в формате E164 пример: +3396360XXXX')
            res()
            print(Fore.YELLOW+"  [e] Выход")
            res()
            tru_701 = input('  Введите номер>>> ')
            os.system('clear')
            os.system('python phoneinfoga.py -n '+tru_701+'')
            res()
            os.system('clear')
            tsu_602 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Phoneinfoga еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests...")
            res()
            os.system('pip install requests')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка bs4...")
            res()
            os.system('pip install bs4')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка html5lib...")
            res()
            os.system('pip install html5lib')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка phonenumbers...")
            res()
            os.system('pip install phonenumbers')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка argparse...")
            res()
            os.system('pip install argparse')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка urllib3...")
            res()
            os.system('pip install urllib3')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Phoneinfoga...")
            res()
            os.system('git clone https://github.com/ExpertAnonymous/PhoneInfoga')
            os.chdir('PhoneInfoga')
            os.system('bash phoneinfoga.sh')
            os.chdir('/data/data/com.termux/files/home/Installer_Files')
            os.system('rm -fr PhoneInfoga')
            os.system('mv /data/data/com.termux/files/home/PhoneInfoga /data/data/com.termux/files/home/Installer_Files')

            os.chdir('/data/data/com.termux/files/home/Installer_Files/PhoneInfoga')
            baner()
            print(Style.BRIGHT,Fore.CYAN+"\n  [Phoneinfoga]")
            res()
            print(Fore.GREEN+'  Введите телефон в формате E164 пример: +3396360XXXX')
            res()
            print(Fore.YELLOW+"  [e] Выход")
            res()
            tru_701 = input('  Введите номер>>> ')
            os.system('clear')
            os.system('python phoneinfoga.py -n '+tru_701+'')
            res()
            os.system('clear')
            tsu_602 = input(' [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')



    if inp == '18':
        os.chdir('/data/data/com.termux/files/home/Installer_Files/trash')
        filename = "holehe"

        if os.path.exists(filename):
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Holehe еще НЕ установлен!")
            time.sleep(2)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Holehe...")
            res()
            os.system('pip3 install holehe')
            os.system('rm -fr /data/data/com.termux/files/home/Installer_Files/trash/holehe')
            os.system('clear')

            baner()
            print(Style.BRIGHT,Fore.CYAN+" [Holehe]")
            res()
            print(Fore.GREEN+'  Введите почту пример: test@gmail.com')
            res()
            print(Fore.YELLOW+"  [e] Выход")
            res()
            tru_801 = input('  Введите почту>>> ')
            if tru_801 == 'e':
                os.system('clear')
            
            else:
                os.system('clear')
                baner()
                os.system('holehe '+tru_801+' --only-used --no-clear')
                res()
                tsu_602 = input('[Нажмите enter чтобы выйти]')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')

        else:
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.GREEN+"~"+Fore.YELLOW+"] Holehe уже установлен!")
            time.sleep(2)
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(0.5)

            baner()
            print(Style.BRIGHT,Fore.CYAN+" [Holehe]")
            res()
            print(Fore.GREEN+'  Введите почту пример: test@gmail.com')
            res()
            print(Fore.YELLOW+"  [e] Выход")
            res()
            tru_801 = input('  Введите почту>>> ')
            if tru_801 == 'e':
                os.system('clear')
            
            else:
                os.system('clear')
                baner()
                os.system('holehe '+tru_801+' --only-used --no-clear')
                res()
                tsu_602 = input('[Нажмите enter чтобы выйти]')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')








    
    

    if inp == '20':
        print(f'\33]0; Installer - Страница [3]\a',
                      end='', flush=True)
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
