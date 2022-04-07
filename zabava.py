import os, time, webbrowser

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
    print(Fore.RED+'[меню <забавы>]')
    print(Fore.GREEN+'', Style.BRIGHT)
    print (" _                 _             _   _               ")
    print ("(_)  _ __    ___  | |_    __ _  | | | |   ___   _ __ ")
    print ("| | | '_ \  / __| | __|  / _` | | | | |  / _ \ | '__|")
    print ("| | | | | | \__ \ | |_  | (_| | | | | | |  __/ | |   ")
    print ("|_| |_| |_| |___/  \__|  \__,_| |_| |_|  \___| |_|   ")
    print ("\n")
    print ("[telegram: @SYPEXHACK]                       [v2.6.0]")
    res()
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
        os.system('xdg-open https://t.me/MR_FOXik')
        os.system('clear')
        

    if inp == '88':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')


    if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break
