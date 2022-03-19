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

#нгрок
os.system('pkg install nodejs-lts -y')
os.system('npm install ngrok')
os.system('clear')
os.system('npm install ngrok -g')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

#фишинг
os.system('git clone https://github.com/KasRoudra/PyPhisher')
os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

#брутфорс
os.system('git clone https://github.com/noob-hackers/ighack')
os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

#блокировка.тер..
os.system('git clone https://github.com/fuckwbored/termuxman')
os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

#камера
os.system('pip install colorama')
os.system('clear')
os.system('git clone https://github.com/AngelSecurityTeam/Cam-Hackers')
os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

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
    print ("    [by @SYPEXHACK]                            [v1.0]")
    time.sleep(2)
    print ('\n\n')
    print ("    [1] тунелирование <ngrok>")
    print ("    [2] фишинг <PyPhisher>")
    print ("    [3] брутфорс <Instagram> [временно не работает]")
    print ("    [4] заблокировать Termux <!!ОПАСНО!!>")
    print ("    [5] просмотр камер <98 стран>")
    print ("\n")
    print ("    [99] обновить[BETA]")
    print ("    [0] выход")
    print ("\n\n")
    inp = input ('  Выбери пункт>>>  ')
    os.system('clear')
    
    if inp == '1':    
        os.system('clear')
        print('[напишите команду< ngrok http [порт] >Пример: ngrok http 8080]')
        break
    
    if inp == '2':   
        print('[ВНИМАНИЕ ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru = input('\n Включили? [y/n] >>> ')
        os.system('clear')
        if tru == 'y':
            os.system('cd $HOME')
            os.chdir('PyPhisher')
            os.system('python3 pyphisher.py')
        if tru == 'n':
            os.system('clear')
            pass
        else:
            os.system('clear')

    if inp == '3':    
        os.system('clear')
        os.chdir('ighack')
        os.system('bash setup')
        os.system('bash ighack.sh')
        os.system('tor')

    if inp == '4':   
        os.system('clear') 
        os.chdir('termuxman')
        os.system('python3 termuxman.py')

    if inp == '5':    
        os.system('clear') 
        os.chdir('Cam-Hackers')
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

