import os, time, webbrowser

from colorama import Fore, Style

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
    print(Style.BRIGHT, Fore.CYAN+"[Telegram: @SYPEXHACK]                         [v2.8.0]")
    res()
    print(Fore.GREEN+"    [1] Ngrok      >>  Тунелирование")
    print(Fore.GREEN+"    [2] Localhost  >>  Тунелирование")
    print(Fore.GREEN+"    [3] PyPhiser   >>  Фишинг")
    print(Fore.GREEN+"    [4] Zphisher   >>  Фишинг")
    print(Fore.GREEN+"    [5] CamPhish   >>  Взлом веб-камеры")
    print(Fore.GREEN+"    [6] Android    >>  Вирус ссылка")
    print(Fore.GREEN+"    [7] Maskphish  >>  Замаскировать ссылку")
    print(Fore.GREEN+"    [8] IP-Tracer  >>  Пробив по IP")
    print(Fore.GREEN+"    [9] Seeker     >>  Узнать местоположения")
    print(Fore.CYAN+"")
    print(Fore.YELLOW+"    [s] Настройки")
    print(Fore.YELLOW+"    [e] Выход")
    res()
    inp = input('  Выбери пункт>>> ')
    os.system('clear')
    

    if inp == '9':
        filename = "seeker"

        if os.path.exists(filename):
            print(f"{filename} существует в текущем каталоге.")
            time.sleep(1.5)
            
            os.system('clear')
            os.system('python seeker.py')
            tsu_901 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')
        
        
        else:
            print(f"{filename} не существует в текущем каталоге.")
            time.sleep(1.5)
            
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
            res()
            time.sleep(1.5)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка dropbear...")
            res()
            os.system('pkg install dropbear -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка openssh...")
            res()
            os.system('pkg install openssh -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка php...")
            res()
            os.system('pkg install php -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка php7...")
            res()
            os.system('pkg install php7 -y')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
            res()
            os.system('git clone https://github.com/thewhiteh4t/seeker.git')
            os.chdir('seeker')
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
            res()
            os.system('chmod 777 install.sh')
            os.system('./install.sh')
            os.system('clear')
            os.system('python seeker.py')
            tsu_901 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')


    
    if inp == 's':
        os.system('cd /data/data/com.termux/files/home/installer/')
        os.system('python set.py')

    

    if inp == 'e':
        os.system('clear')
        print('\n')
        print(Fore.CYAN+'Спасибо за использование Installer')
        res()
        break