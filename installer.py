import os, time

print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

#питон2
os.system('pkg install python2')

#нгрок
os.system('git clone https://github.com/tchelospy/termux-ngrok.git')

#фишинг
os.system('git clone https://github.com/KasRoudra/PyPhisher')

#брутфорс
os.system('git clone https://github.com/noob-hackers/ighack')

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
    print ("    [1] ngrok")
    print ("    [2] фишинг")
    print ("    [3] брутфорс <Instagram>")
    print ("    [4] заблокировать Termux <!!ОПАСНО!!>")
    print ("    [5] просмотр камер <98 стран>")
    print ("\n")
    print ("    [99] обновить")
    print ("    [0] выход")
    print ("\n\n")
    inp = input ('  Выбери пункт>>>  ')
    os.system('clear')
    
    if inp == '1':    
        time.sleep(1)
        os.chdir('termux-ngrok')
        os.system('chmod +x termux-ngrok.sh')
        os.system('./termux-ngrok.sh')
    
    if inp == '2':   
        print('[ВНИМАНИЕ ПЕРЕД ЗАПУСКОМ ВКЛЮИТЕ ТОЧКУ ДОСТУПА И МОБ ИНТЕРНЕТ]')
        tru = input('\n Включили? [y/n] >>> ')
        if tru == 'y':
            os.system('cd $HOME')
            os.chdir('cd PyPhisher')
            os.system('python3 pyphisher.py')
        if tru == 'n':
            os.system('clear')
            pass

    if inp == '3':    
        time.sleep(1)
        os.chdir('ighack')
        os.system('bash setup')
        os.system('bash ighack.sh')

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

