import os, time, webbrowser

we = '<НЕ установлен>'
    
re = '<НЕ установлен>'

de = '<НЕ утсановлен>'

ke = '<НЕ установлен>'

te = '<НЕ установлен>'

le = '<НЕ установлен>'

os.system('clear')

from colorama import Fore, Style

print ('\n')
def res():
    print(Style.RESET_ALL)
    
while True:
    os.system('clear')
    print(Fore.RED+'[меню <файлы>]')
    print('\n')
    print(Fore.GREEN+'')
    print (" #                 #          ##    ##              ")
    print ("                   #           #     #              ")
    print ("##   ###    ###   ###    ###   #     #     ##   ### ")
    print (" #   #  #  ##      #    #  #   #     #    # ##  #  #")
    print (" #   #  #    ##    #    # ##   #     #    ##    #   ")
    print ("###  #  #  ###      ##   # #  ###   ###    ##   #   ")
    print ('\n')
    print ("[telegram: @SYPEXHACK]                      [v2.3.1]")
    res()
    print ('\n')
    print (Fore.YELLOW+'    [1] установить php '+we)
    print (Fore.YELLOW+'    [2] установить ssh '+re)
    print (Fore.YELLOW+'    [3] установить requests '+de)
    print (Fore.YELLOW+'    [4] установить lolcat '+ke)
    print (Fore.YELLOW+'    [5] установить proot '+te)
    print (Fore.YELLOW+'    [6] установить nano '+le)
    print (Fore.CYAN+"\n                                     ╔═════════════╗")
    print (Fore.CYAN+'    [77] поддержка автора            ║'+Fore.YELLOW+' утилиты'+Fore.CYAN+'[91] ║')
    print (Fore.CYAN+'    [66] тг канал автора             ║'+Fore.YELLOW+' забавы ' +Fore.CYAN+'[92] ║')
    print (Fore.CYAN+'    [99] обновить                    ║'+Fore.GREEN +'>файлы<'  +Fore.CYAN+' [93] ║')
    print (Fore.CYAN+'    [00] выход                       ╚═════════════╝')
    res()
    inp = input ('  Выбери пункт>>> ')
    os.system('clear')

    if inp == '91':
        os.system('clear')
        os.system('python3 tool.py')
        

    if inp == '92':
        os.system('clear')
        os.system('python3 zabava.py')


    if inp == '93':
        os.system('clear')


    if inp == '1':
        os.system('pkg install php -y')
        os.system('pkg install php7 -y')
        we = '<установлен>'
        os.system('clear')

    if inp == '2':
        os.system('pkg install dropbear -y')
        os.system('pkg install openssh -y')
        re = '<установлен>'
        os.system('clear')


    if inp == '3':
        os.system('pip install requests')
        de = '<установлен>'
        os.system('clear')

    if inp == '4':
        os.system('pip install lolcat')
        ke = '<установлен>'
        os.system('clear')

    if inp == '5':
        os.system('pkg install proot')
        te = '<установлен>'
        os.system('clear')

    if inp == '6':
        os.system('pkg install nano')
        le = '<установлен>'
        os.system('clear')


    if inp == '77':
        os.system('xdg-open https://www.donationalerts.com/r/legends_never_die')


    if inp == '99':    
        os.system('clear')
        print ("Загрузка...")
        time.sleep(3)
        os.chdir('updater-for-installer')
        os.system('python3 update.py')

        
    if inp == '66':
        os.system('xdg-open https://t.me/SYPEXHACK')
        os.system('clear')
    if inp == '00':
        os.system('clear')
        print('Спасибо за использование [installer]')
        break
