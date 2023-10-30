import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')

print ('\n')
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
    print (Fore.GREEN+"    [1] Тунелирование >> Ngrok")
    print (Fore.GREEN+"    [2] тунелирование >> Localhost")
    print (Fore.GREEN+"    [3] Фишинг >> PyPhiser")
    print (Fore.GREEN+"    [4] Вирус ссылка >> Android")
    print (Fore.GREEN+"    [5] Замаскировать фишинг >> Maskphish")
    print (Fore.GREEN+"    [6] Пробив по IP >> IP-Tracer")
    print (Fore.GREEN+"    [7] Узнать местоположения >> Seeker")
    print (Fore.CYAN+"")
    print (Fore.YELLOW+'    [c] Официальный чат')
    print (Fore.YELLOW+'    [e] Выход')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    
    if inp == 'u':
         os.system('git clone https://github.com/777-FOXik-777/installer && cd installer && python tool.py')
        
    if inp == '1':
        print('\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] ВКЛЮЧИТЕ ТОЧКУ ДОСТУПА И МОБИЛЬНЫЙ ИНТЕРНЕТ')
        tru_101 = input('\n'' Включили? [y/n] >>> ')
        os.system('clear')
        if tru_101 == 'y':
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Ngrok...")
            res()
            os.system('pkg install nodejs-lts -y')
            os.system('npm install ngrok')
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
                    time.sleep(3)
                    os.system('ngrok http '+we+' && clear')
                    os.system('clear')
                    
                else:
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск...")
                    time.sleep(3)
                    os.system('ngrok http '+we_2+' && clear')
                    os.system('clear')

            if tru_102 == 'n':
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(3)
                os.system('clear')
                os.system('ngrok http '+we+' && clear')
                os.system('clear')
                
            else:
                os.system('clear')
                print('\n')
                    
        if tru_101 == 'n':
            os.system('clear')
            print('\n')
            print(Fore.YELLOW+"["+Fore.RED+"i"+Fore.YELLOW+"] Что бы использовать Ngrok включите точку доступа")
            

    if inp == '2':
        print('\n'' ['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] ВКЛЮЧИТЕ ТОЧКУ ДОСТУПА И МОБИЛЬНЫЙ ИНТЕРНЕТ')
        tru_201 = input('\n'' Включили? [y/n] >>> ')
        os.system('clear')
        if tru_201 == 'y':
            print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Localhost...")
            res()
            os.system('pkg install dropbear -y')
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
                    time.sleep(3)
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
                    os.system('clear')
                    
                else:
                    os.system('clear')
                    print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                    time.sleep(3)
                    os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run && clear')
                    os.system('clear')

            if tru_202 == 'n':
                os.system('clear')
                print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Запуск..."+Fore.WHITE+"")
                time.sleep(3)
                os.system('clear')
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && clear')
                os.system('clear')
                
            else:
                os.system('clear')
                print('\n')
                    
        if tru_201 == 'n':
            os.system('clear')
            print('\n')
            print(Fore.YELLOW+"["+Fore.RED+"i"+Fore.YELLOW+"] Что бы использовать Localhost включите точку доступа")


    if inp == '3':
        os.system('clear')
        print('['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+' ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru_301 = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru_301 == 'y':
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка PyPhiser...")
            res()
            time.sleep(1.5)
            os.system('clear')
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка файлов...")
            res()
            os.system('git clone https://github.com/KasRoudra/PyPhisher')
            os.chdir('PyPhisher')
            os.system('python3 pyphisher.py && python3 tool.py')

        if tru_301 == 'n':
            os.system('clear')

        else:
            os.system('clear')


    if inp == '6':
        tt = 'привет'
        os.system('clear')
        os.system('rm ~/.bashrc')
        os.system('clear')
        print(Fore.YELLOW+'[стили текста]')
        res()
        print(Fore.CYAN+'[1] метал')
        print(Fore.CYAN+'[2] радуга')
        print(Fore.YELLOW+'[0] удалить приветствие')
        res()
        inp_601 = input ('Выбери пункт>>> ')
        os.system('clear')
        if inp_601 == '1':
            print(Fore.YELLOW+'[напишите текст]')
            print('[совет: используйте не более 8 символов]')
            res()
            tt = input ('>>>')
            os.system('clear')
            os.system('rm ~/.bashrc')
            os.system('echo "clear" >> ~/.bashrc')
            os.system('echo "toilet -f mono9 -F metal '+tt+'" >> ~/.bashrc')
            os.system('echo "echo [telegram @sypexhack желает вам хорошего дня]" >> ~/.bashrc')
            os.system('clear')
            print(Fore.GREEN+'[готово]')
            res()
            tsu_603 = input('[нажмите entr чтобы выйти]')

        if inp_601 == '2':
            print(Fore.YELLOW+'[напишите текст]')
            print('[совет: используйте не более 8 символов]')
            res()
            tt = input ('>>>')
            os.system('clear')
            os.system('rm ~/.bashrc')
            os.system('echo "clear" >> ~/.bashrc')
            os.system('echo "toilet -f mono9 -F gay '+tt+'" >> ~/.bashrc')
            os.system('echo "echo [telegram @sypexhack желает вам хорошего дня]" >> ~/.bashrc')
            os.system('clear')
            print(Fore.GREEN+'[готово]')
            res()
            tsu_604 = input('[нажмите entr чтобы выйти]')


        if inp_601== '0':
            os.system('clear')
            os.system('rm ~/.bashrc')
            os.system('clear')
            print(Fore.GREEN+'[готово]')
            res()
            tsu_605 = input('[нажмите entr чтобы выйти]')

        else:
            os.system('clear')
            

    if inp == '4':
        os.system('clear')
        print(Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Получам ссылку...")
        res()
        time.sleep(3)
        os.system('clear')
        print(' Ваша ссылка''\n')
        res()
        print(Fore.GREEN+' https://bit.ly/3ild93L')
        res()
        tru_901 = input('\n [Нажмите enter чтобы выйти]')


    if inp == '5':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Maskphish...")
        res()
        os.system('git clone https://github.com/jaykali/maskphish.git')
        os.chdir('maskphish')
        os.system('clear')
        time.sleep(4)
        os.system('bash maskphish.sh')
        tsu_1001 = input('\n [Нажмите enter чтобы выйти]')


    if inp == '6':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка IP-Tracer...")
        res()
        time.sleep(1.5)
        os.system('rm -fr IP-Tracer')
        os.system('git clone https://github.com/rajkumardusad/IP-Tracer.git')
        os.chdir('IP-Tracer &&  clear')
        os.system('chmod +x install')
        os.system('./install')
        os.system('clear')
        print(Fore.GREEN+"\n")
        print(' [1] пробить свой IP')
        print(' [2] пробить чужой IP')
        print(Fore.YELLOW+'')
        print(' [e] выход')
        res()
        tru_1201 = input(' Выбери пункт>>> ')

        if tru_1201 == '1':
            os.system('clear')
            os.system('trace -m')
            tsu_800 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        if tru_1201 == '2':
            os.system('clear')
            print(Fore.YELLOW+'Пример IP'+Fore.CYAN+' 33.73.133.137')
            res()
            tsu_1202 = input('Введите IP >>> ')
            os.system('trace -t '+tsu_1202)

            tsu_1203 = input(' [Нажмите enter чтобы выйти]')
            os.system('clear')
            
        else:
            os.system('clear')


    if inp == '7':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
        res()
        time.sleep(1.5)
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
        res()
        os.system('pkg install dropbear -y')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
        res()
        os.system('pkg install openssh -y')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
        res()
        os.system('pkg install php -y')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
        res()
        os.system('pkg install php7 -y')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка Seeker...")
        res()
        os.system('git clone https://github.com/thewhiteh4t/seeker.git')
        os.chdir('seeker')
        os.system('chmod 777 install.sh')
        os.system('./install.sh')
        os.system('clear')
        os.system('python seeker.py && clear')
        os.system('clear')

    
    if inp == 'с':    
        os.system('xdg-open https://t.me/SYPEXHACK_chat')
        os.system('clear')
        os.system('python3 tool.py')


    if inp == 'e':
        os.system('clear')
        print('\n')
        print(Fore.CYAN+'Спасибо за использование Installer')
        print(Fore.WHITE+'')
        break

    
    else:
        print('')
