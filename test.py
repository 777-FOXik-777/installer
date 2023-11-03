import os, time, webbrowser, random

from colorama import Fore, Style, Back

print ('\n')

def res():
    print(Style.RESET_ALL)

def baner():
    print(Fore.RED+'', Style.BRIGHT)
    print (" _                 _             _   _               ")
    print ("(_)  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print ("| | | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print ("| | | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|_| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print ("\n")
    print ("[telegram: @SYPEXHACK]                       [v2.6.0]")
    res()


while True:
    os.system('clear')
    baner()
    print (Fore.YELLOW+"    [1] матрица ")
    print (Fore.YELLOW+"    [2] паравозик")
    print (Fore.YELLOW+"    [3] карта мира")
    print (Fore.YELLOW+"    [4] огонь")
    print (Fore.YELLOW+"    [5] часы")
    print (Fore.YELLOW+"    [6] красивый текст")
    print (Fore.CYAN+"\n                                     ╔═════════════╗")
    print (Fore.CYAN+'    [77] поддержка автора            ║'+Fore.YELLOW+' утилиты '+Fore.CYAN+'[91]║')
    print (Fore.CYAN+'    [88] тг канал автора             ║'+Fore.GREEN+'>забавы<'+Fore.CYAN+' [92]║')
    print (Fore.CYAN+'    [99] тех поддержка               ║'+Fore.YELLOW+' файлы  '+Fore.CYAN+' [93]║')
    print (Fore.CYAN+'    [00] выход                       ╚═════════════╝')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '11':
        baner()
        inp = input ('  ttr')



    if inp == '33':
        os.system('cd PyPhisher')
        if os.path.exists(test_path):
            if os.path.isfile(test_path):
                os.system('clear')
                print('файл есть')
                time.sleep(3)
                              
                os.system('clear')
                os.system('python3 pyphisher.py')
                tsu_302 = input('\n [Нажмите enter чтобы выйти]')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')
    
            elif os.path.isdir(test_path):
                print ("Файла не найден")
                time.sleep(3)
                
                os.system('clear')
                print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка PyPhiser...")
                res()
                time.sleep(1.5)
                os.system('git clone https://github.com/KasRoudra/PyPhisher')
                os.chdir('PyPhisher')
                os.system('clear')
                os.system('python3 pyphisher.py')
                tsu_302 = input('\n [Нажмите enter чтобы выйти]')
                os.chdir('/data/data/com.termux/files/home/installer')
                os.system('clear')
        else:
            print('Объект не найден')


    
    if inp == '91':
        os.system('clear')
        os.system('python3 tool.py')


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
        inp_5 = input ('нажмите entr чтобы выйти')
        if inp_5 == '':
            os.system('clear')
        else:
            os.system('clear')

    if inp == '6':
        lo = 'SYPEXHACK'
        os.system('clear')
        print(Fore.YELLOW+'[стили текста]')
        res()
        print(Fore.CYAN+'[1] метал')
        print(Fore.CYAN+'[2] радуга')
        res()
        inp_2 = input ('Выбери пункт>>> ')
        os.system('clear')
        if inp_2 == '1':
            lo = 'SYPEXHACK'
            print(Fore.YELLOW+'[напишите текст]')
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
            lo = 'SYPEXHACK'
            print(Fore.YELLOW+'[напишите текст]')
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
        os.system('xdg-open https://t.me/perehodos')
        os.system('clear')
        

    if inp == '88':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')


    if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break
