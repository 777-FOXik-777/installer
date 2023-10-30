import os, time, webbrowser

from colorama import Fore, Style

os.system('clear')
print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    print(Fore.CYAN+'', Style.BRIGHT)
    print (" _                 _             _   _               ")
    print ("(_)  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print ("| | | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print ("| | | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|_| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print ("\n")
    print ("[Telegram: @SYPEXHACK]                       [v2.7.1]")
    res()
    print (Fore.GREEN+"    [01] Тунелирование <ngrok>")
    print (Fore.GREEN+"    [02] тунелирование <localhost>")
    print (Fore.GREEN+"    [03] фишинг")
    print (Fore.GREEN+"    [04] ддос")
    print (Fore.GREEN+"    [05] бомбер <мини>")
    print (Fore.GREEN+"    [06] приветствие")
    print (Fore.GREEN+"    [08] просмотр взломаных камер")
    print (Fore.GREEN+"    [09] вирус ссылка")
    print (Fore.GREEN+"    [10] замаскировать фишинг")
    print (Fore.GREEN+"    [11] пробив по номеру")
    print (Fore.GREEN+"    [12] пробив по ip")
    print (Fore.GREEN+"    [13] пробив инстаграм")
    print (Fore.GREEN+"    [14] соц-сети по нику")
    print (Fore.GREEN+"    [15] местоположения по ссылке")
    print (Fore.CYAN+"\n")
    print (Fore.YELLOW+'    [s] Подписатся на Telegram')
    print (Fore.YELLOW+'    [c] Официальный чат')
    print (Fore.YELLOW+'    [e] Выход')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    
    if inp == 'u':
         os.system('git clone https://github.com/777-FOXik-777/installer && cd installer && python tool.py')
        
    if inp == '1':
        print('['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+'] ПЕРЕД ЗАПУСКОМ ВКЛЮЧИТЕ ТОЧКУ ДОСТУПА И МОБИЛЬНЫЙ ИНТЕРНЕТ')
        tru_101 = input('\n''Включили? [y/n] >>> ')
        os.system('clear')
        if tru_101 == 'y':
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка ngrok...")
            res()
            os.system('pkg install nodejs-lts -y')
            os.system('npm install ngrok')
            os.system('npm install ngrok -g')
            we  = '8080'
            os.system('clear')
            print('[Стандартный порт 8080]')
            tru_102 = input('\n''Изменить порт? [y/n] >>> ')
            if tru_102 == 'y':
                os.system('clear')
                we_2 = input('Введите порт>>> ')
                if we_2 == '':
                    os.system('clear')
                    print('Вы ничего не ввели!')
                    print('\n''Использую стандартный порт ['+we+']')
                    time.sleep(7)
                    os.system('clear')
                    os.system('ngrok http '+we+' && python3 tool.py')
                else:
                    os.system('clear')
                    os.system('ngrok http '+we_2+' && python3 tool.py')

            if tru_102 == 'n':
                os.system('clear')
                os.system('ngrok http '+we+'&& python3 tool.py')

            else:
                os.system('clear')
                os.system('ngrok http '+we+' && python3 tool.py')

        if tru_101 == 'n':
            os.system('clear')
            print('['Fore.RED+'Пожалуйста включите мобильную точку доступа и повторите'']')
            time.sleep(3)
            os.system('clear')
            os.system('python3 tool.py')
            print ('\n')
            print (Fore.YELLOW+"["+Fore.RED+"i"+Fore.YELLOW+"] Выбран не существующий пункт!")

        else:
            os.system('clear')
            os.system('python3 tool.py')

    if inp == '2':
        os.system('clear')
        print('['+Fore.RED+'ВНИМАНИЕ!'+Fore.WHITE+'] ПЕРЕД ЗАПУСКОМ ВКЛЮЧИТЕ ТОЧКУ ДОСТУПА И МОБИЛЬНЫЙ ИНТЕРНЕТ')
        tru_201 = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru_201 == 'y':
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка localhost...")
            res()
            os.system('pkg install dropbear -y')
            os.system('pkg install openssh -y')
            qw = '8080'
            os.system('clear')
            print('[<localhost> стандартный порт:8080]')
            tru_202 = input('\n Изменить порт? [y/n] >>> ')
            if tru_202 == 'y':
                os.system('clear')
                qw_2 = input('Введите порт>>> ')
                if qw_2 == '':
                    os.system('clear')
                    print(' Вы ничего не ввели ')
                    print('[Порт '+qw+']')
                    time.sleep(4)
                    os.system('clear')
                    print(Fore.GREEN+'[ваша ссылка находится в самом нижнем ряде]')
                    print(Fore.YELLOW+'[если ссылка не появилась, а последний символ')
                    print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                    res()
                    time.sleep(4)
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && python3 tool.py')
                else:
                    os.system('clear')
                    print(Fore.GREEN+'[ваша ссылка находится в самом нижнем ряде]')
                    print(Fore.YELLOW+'[если ссылка не появилась, а последний символ')
                    print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                    res()
                    time.sleep(4)
                    os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run && python3 tool.py')

            if tru_202 == 'n':
                os.system('clear')
                print(Fore.GREEN+'[Ваша ссылка находится в самом нижнем ряде]')
                print(Fore.YELLOW+'[если ссылка не появилась, а последний символ')
                print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                res()
                time.sleep(4)
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && python3 tool.py')
            else:
                os.system('clear')
                print(Fore.GREEN+'[ваша ссылка находится в самом нижнем ряде]')
                print(Fore.YELLOW+'[если ссылка не появилась, а последний символ')
                print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                res()
                time.sleep(4)
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run && python3 tool.py')
                
        if tru_201 == 'n':
            os.system('clear')
            print(Fore.RED+'[пожалуйста включите моб. Точку доступа и повторите]')
            time.sleep(3)

        else:
            os.system('clear')



    if inp == '3':
        os.system('clear')
        print('['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+' ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru_301 = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru_301 == 'y':
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка фишинг...")
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


    if inp == '4':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка ддос...")
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
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка файлов...")
        res()
        os.system('git clone https://github.com/lamer112311/Doser')
        os.chdir('Doser')
        os.system('bash install.sh')
        os.system('python doser.py && python3 tool.py')


    if inp == '5':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка бомбер...")
        res()
        os.system('pip install db0mb3r')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.GREEN+"ВНИМАНИЕ"+Fore.YELLOW+"] вас будет переброшено на сайт просто подождите 5-10сек.")
        res()
        time.sleep(5)
        os.system('bomber')


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
            

    if inp == '8':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка взломаных камер...")
        res()
        time.sleep(1.5)
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка файлов...")
        res()
        os.system('pip install requests')
        os.system('git clone https://github.com/AngelSecurityTeam/Cam-Hackers') 
        os.chdir('Cam-Hackers')
        os.system('clear')
        os.system('chmod +x *')
        os.system('python cam-hackers.py')
        tsu_801 = input('[нажмите entr чтобы выйти]')


    if inp == '9':
        os.system('clear')
        print(Fore.GREEN+'[Генерируется ссылка...]')
        res()
        time.sleep(3)
        os.system('clear')
        print('ваша ссылка')
        res()
        print(Fore.GREEN+'https://bit.ly/3ild93L')
        res()
        tru_901 = input('\n [Нажмите enter чтобы выйти]')


    if inp == '10':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка маск. фишинг...")
        res()
        os.system('git clone https://github.com/jaykali/maskphish.git')
        os.chdir('maskphish')
        os.system('clear')
        print('Инструкция находиться по ссылке:')
        print(Fore.GREEN+'https://telegra.ph/maskphish-04-08')
        time.sleep(4)
        os.system('bash maskphish.sh')
        tsu_1001 = input('\n [Нажмите enter чтобы выйти]')


    if inp == '11':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка пробив телефона...")
        res()
        time.sleep(1.5)
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка файлов...")
        res()
        os.system('git clone https://github.com/Wes974/PhoneInfoga')
        os.chdir('PhoneInfoga')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка доп. файлов...")
        res()
        os.system('pip install -r requirements.txt')
        os.system('clear')
        print('[Введите номер телефона в формате: +(код)##########]')
        print('[Пример: +71237689098]')
        tsu_1101 = input('\n Введите номер >>> ')
        if 1101 == '':
            os.system('clear')
            print('[вы ничего не ввели]')
            res()
            tsu_1103 = input('[нажмите entr чтобы выйти]')

        else:
            os.system('clear')
            os.system('python phoneinfoga.py -n '+tsu_1101)
            tsu_1103 = input('[нажмите entr чтобы выйти]')


    if inp == '12':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка пробив по ip...")
        res()
        time.sleep(1.5)
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка файлов...")
        res()
        os.system('rm -fr IP-Tracer')
        os.system('git clone https://github.com/rajkumardusad/IP-Tracer.git')
        os.chdir('IP-Tracer')
        os.system('chmod +x install')
        os.system('./install')
        os.system('clear')
        print(Fore.YELLOW+" ")
        print('[1] пробить свой ip')
        print('[2] пробить чужой ip')
        print('[0] выход')
        res()
        tru_1201 = input('Выбери пункт>>> ')

        if tru_1201 == '1':
            os.system('clear')
            os.system('trace -m')
            tsu_800 = input('[нажмите entr чтобы выйти]')
            os.system('cd && rm -fr installer && rm -fr installer.py && rm -fr tool.py && rm -fr fail.py && rm -fr zabava.py && git clone https://github.com/777-FOXik-777/installer && cd installer && python3 tool.py')

        if tru_1201 == '2':
            os.system('clear')
            print(Fore.YELLOW+'Пример IP 33.73.133.137')
            res()
            tsu_1202 = input('введите ip >>> ')
            os.system('trace -t '+tsu_1202)

            tsu_1203 = input('[нажмите entr чтобы выйти]')
            os.system('cd && rm -fr installer && rm -fr installer.py && rm -fr tool.py && rm -fr fail.py && rm -fr zabava.py && git clone https://github.com/777-FOXik-777/installer && cd installer && python3 tool.py')

        else:
            os.system('cd && rm -fr installer && rm -fr installer.py && rm -fr tool.py && rm -fr fail.py && rm -fr zabava.py && git clone https://github.com/777-FOXik-777/installer && cd installer && python3 tool.py')


    if inp == '13':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка пробив Instagram...")
        res()
        time.sleep(1.5)
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка файлов...")
        res()
        os.system('git clone https://github.com/th3unkn0n/osi.ig')
        os.chdir('osi.ig')
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка доп. файлов...")
        res()
        os.system('python3 -m pip install -r requirements.txt')
        os.system('clear')
        print(Fore.GREEN+'[Введите ник в инстаграм]')
        print(Fore.CYAN+'[Пример: ververa]')
        res()
        tsu_1301 = input('Введите ник>>> ')
        if tsu_1301 == '':
            os.system('clear')
            print('[вы ничего не ввели]')
            res()
            tsu_1302 = input('[нажмите entr чтобы выйти]')
            os.system('cd && rm -fr installer && rm -fr installer.py && rm -fr tool.py && rm -fr fail.py && rm -fr zabava.py && git clone https://github.com/777-FOXik-777/installer && cd installer && python3 tool.py')

        else:
            os.system('clear')
            os.system('python3 main.py -u '+tsu_1301)
            tsu_1303 = input('[нажмите entr чтобы выйти]')
            os.system('cd && rm -fr installer && rm -fr installer.py && rm -fr tool.py && rm -fr fail.py && rm -fr zabava.py && git clone https://github.com/777-FOXik-777/installer && cd installer && python3 tool.py')


    if inp == '14':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка соц.-ник...")
        res()
        time.sleep(1.5)
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка файлов...")
        res()
        os.system('git clone https://github.com/issamelferkh/userrecon.git')
        os.chdir('userrecon')
        os.system('clear')
        os.system('chmod +x userrecon.sh')
        os.system('bash userrecon.sh')
        res()
        tru_1401 = input('[нажмите entr чтобы выйти]')


    if inp == '15':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка seeker...")
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
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка файлов...")
        res()
        os.system('git clone https://github.com/thewhiteh4t/seeker.git')
        os.chdir('seeker')
        os.system('chmod 777 install.sh')
        os.system('./install.sh')
        os.system('clear')
        os.system('echo "clear" >> ~/.bashrc && echo "echo [ваша ссылка находится в самом нижнем ряде]" >> ~/.bashrc && echo "echo [если ссылка не появилась, а последний символ" >> ~/.bashrc && echo "echo знак вопроса напишите [yes]" >> ~/.bashrc && echo "rm ~/.bashrc" >> ~/.bashrc && echo "ssh -R 80:localhost:8080 nokey@localhost.run && cd && cd installer && python3 tool.py" >> ~/.bashrc')
        print(Fore.YELLOW+'[включите моб. точку доступа]')
        time.sleep(4)
        print(Fore.GREEN+'[чтоб получить ссылку создайте второй сезон]')
        print(' ')
        time.sleep(2)
        os.system('python seeker.py && cd installer && python3 tool.py')

    if inp == 's':    
        os.system('xdg-open https://t.me/SYPEXHACK_chat')
        os.system('clear')
        os.system('python3 tool.py')

    if inp == 'c':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')
        os.system('python3 tool.py')


    if inp == 'e':
        os.system('clear')
        print(Fore.YELLOW+'Спасибо за использование Installer')
        break

    else:
        os.system('clear')
        print ('\n')
        print (Fore.YELLOW+"["+Fore.RED+"i"+Fore.YELLOW+"] Выбран не существующий пункт!")
