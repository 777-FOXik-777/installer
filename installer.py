import os, time

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


print ('\n')

while True:
    print('\n\n')
    print (" #                 #          ##    ##              ")
    print ("                   #           #     #              ")
    print ("##   ###    ###   ###    ###   #     #     ##   ### ")
    print (" #   #  #  ##      #    #  #   #     #    # ##  #  #")
    print (" #   #  #    ##    #    # ##   #     #    ##    #   ")
    print ("###  #  #  ###      ##   # #  ###   ###    ##   #   ")
    print ('\n')
    print ("[telegram: @SYPEXHACK]                        [v1.0]")
    time.sleep(2)
    print ('\n\n')
    print ("    [1] тунелирование <ngrok>")
    print ("    [2] тунелирование <localhost>")
    print ("    [3] фишинг <PyPhisher>")
    print ("    [4] [временно не доступно]")
    print ("    [5] заблокировать Termux <!!ОПАСНО!!>")
    print ("    [6] просмотр взломаных камер <CAM-HACKERS>")
    print ("\n")
    print ("    [99] обновить[BETA]")
    print ("    [0] выход")
    print ("\n\n")
    inp = input ('  Выбери пункт>>>  ')
    os.system('clear')
    
    if inp == '1':
        os.system('pkg install nodejs-lts -y')
        os.system('clear')
        os.system('npm install ngrok')
        os.system('clear')
        os.system('npm install ngrok -g')
        os.system('clear')
        print ('[установка нужных файлов]')
        time.sleep(3)
        os.system('clear')
        print('[напишите команду< ngrok http [порт] >Пример: ngrok http 8080]')
        break
    
    if inp == '2':   
        os.system('clear')
        print('[ВНИМАНИЕ ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru_2 = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru_2 == 'y':
            print ('[установка нужных файлов]')
            time.sleep(3)
            
            os.system('pkg install dropbear -y')
            print ('[установка нужных файлов]')
            time.sleep(3)
            os.system('pkg install openssh -y')
            os.system('clear')
            
            print('[Перед запуском выберете порт стандартный порт:8080]')
            tru_3 = input('\n Изменить порт? [y/n] >>> ')
            if tru_3 == 'y':
                os.system('clear')
                qw = 8080
                qw = input('Введите порт>>>')
                if qw == '':
                    print(' Вы ничего не ввели ')
                    time.sleep(2.5)
                    os.system('clear')
                    print(' Порт '+qw)
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
                    os.system('yes')
                else:
                    os.system('ssh -R 80:localhost:'+qw+' nokey@localhost.run')
                    

            if tru_3 == 'n':
                os.system('clear')
                os.system('ssh -R 80:localhost:8080 nokey@localhost.run')
                os.system('yes')
            else:
                os.system('clear')
                os.system('ssh -R 80:localhost:8080 nokey@localhost.run')
                os.system('yes')

        if tru_2 == 'n':
            os.system('clear')
            pass
        else:
            os.system('clear')

    if inp == '3':   
        os.system('clear')
        print('[ВНИМАНИЕ ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
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

    if inp == '99':    
        os.system('git clone https://github.com/777-FOXik-777/installer')
        os.system('clear')
        print ("Загрузка...")
        time.sleep(3)
        os.chdir('installer')
        os.system('python3 installer.py')
        os.system('clear')
        
    if inp == '0':
        os.system('clear')
        break
        
    if inp < '0':
        os.system('clear')
        pass

