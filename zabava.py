import os, time, webbrowser

os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')
os.system('pkg install cmatrix')

os.system('pkg install sl')
os.system('pkg install tty-clock')

os.system('clear')
print ('[установка нужных файлов]')
time.sleep(3)
os.system('clear')

os.system('pkg install libcaca -y')
os.system('pkg install toilet')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
    print(Fore.RED+'[меню <забавы>]')
    print('\n')
    print(Fore.GREEN+'')
    print (" #                 #          ##    ##              ")
    print ("                   #           #     #              ")
    print ("##   ###    ###   ###    ###   #     #     ##   ### ")
    print (" #   #  #  ##      #    #  #   #     #    # ##  #  #")
    print (" #   #  #    ##    #    # ##   #     #    ##    #   ")
    print ("###  #  #  ###      ##   # #  ###   ###    ##   #   ")
    print ('\n')
    print ("[telegram: @SYPEXHACK]                      [v2.1.0]")
    res()
    time.sleep(1)
    print ('\n')
    print (Fore.YELLOW+"    [1] матрица ")
    print (Fore.YELLOW+"    [2] паравозик")
    print (Fore.YELLOW+"    [3] карта мира")
    print (Fore.YELLOW+"    [4] огонь")
    print (Fore.YELLOW+"    [5] часы")
    print (Fore.YELLOW+"    [6] красивый текст")
    print (Fore.CYAN+"\n                                     ╔═════════════╗")
    print (Fore.CYAN+'    [77] поддержка автора            ║'+Fore.YELLOW+' утилиты '+Fore.CYAN+'[91]║')
    print (Fore.CYAN+'    [66] тг канал автора             ║'+Fore.GREEN+'>забавы<'+Fore.CYAN+' [92]║')
    print (Fore.CYAN+'    [99] обновить[BETA]              ║'+Fore.YELLOW+' файлы  '+Fore.CYAN+' [93]║')
    print (Fore.CYAN+'    [00] выход                       ╚═════════════╝')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '91':
        os.system('clear')
        os.system('python3 installer.py')


    if inp == '92':
        os.system('clear')


    if inp == '93':
        os.system('clear')
        os.system('python3 fail.py')



    if inp == '1':
        os.system('cmatrix')


    if inp == '2':
        os.system('sl')

    if inp == '3':
        os.system('telnet mapscii.me')

    if inp == '4':
        os.system('cacafire')


    if inp == '5':
        os.system('tty-clock')


    if inp == '6':
        lo = 'SYPEXHACK'
        os.system('clear')
        print(Fore.YELLOW+'[выберете стиль]')
        res()
        print('[1] метал')
        print('[2] радуга')
        print('\n')
        inp_2 = input ('Выбери пункт>>> ')
        os.system('clear')
        if inp_2 == '1':
            print(Fore.YELLOW+'[напишите текст <на английском>]')
            res()
            lo = input ('>>>')
            os.system('clear')
            os.system('toilet -f mono9 -F metal '+lo)
            inp_4 = input ('нажмите entr чтобы выйти')
            if inp_4 == '':
                os.system('clear')
            else:
                os.system('clear')


        if inp_2 == '2':
            print(Fore.YELLOW+'[напишите текст <на английском>]')
            res()
            lo = input ('>>>')
            os.system('clear')
            os.system('toilet -f mono9 -F gay '+lo)
            inp_3 = input ('нажмите entr чтобы выйти')
            if inp_3 == '':
                os.system('clear')
            else:
                os.system('clear')
        else:
            os.system('clear')


    if inp == '77':
        os.system('xdg-open https://www.donationalerts.com/r/legends_never_die')


    if inp == '99':    
        os.system('git clone https://github.com/777-FOXik-777/installer')
        os.system('clear')
        print ("Загрузка...")
        time.sleep(3)
        os.chdir('installer')
        os.system('python3 zabava.py')
        
    if inp == '66':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')
    if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break


